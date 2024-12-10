import maya.cmds as cmds

def create_locators_on_curve(n):
    """
    Crée N locators équidistants entre le premier et le dernier point d'une courbe sélectionnée.
    
    :param n: Nombre de locators à créer.
    """
    # Vérifier la sélection
    selection = cmds.ls(selection=True)
    
    if not selection:
        cmds.warning("Veuillez sélectionner une courbe.")
        return
    
    curve = selection[0]
    
    # Vérifier si l'objet sélectionné est une courbe
    if not cmds.objectType(cmds.listRelatives(curve, shapes=True)[0], isType="nurbsCurve"):
        cmds.warning("Veuillez sélectionner une courbe NURBS.")
        return
    
    # Obtenir le paramètre du premier et du dernier point de la courbe
    start_param = cmds.getAttr(f"{curve}.minValue")
    end_param = cmds.getAttr(f"{curve}.maxValue")
    
    # Calculer l'intervalle paramétrique
    param_step = (end_param - start_param) / (n - 1)
    
    locators = []
    
    for i in range(n):
        # Calculer la position paramétrique le long de la courbe
        param = start_param + (i * param_step)
        
        # Trouver la position correspondante sur la courbe
        point = cmds.pointOnCurve(curve, pr=param, position=True)
        
        # Créer un locator à cette position
        locator = cmds.spaceLocator(name=f"locator_{i+1}")[0]
        cmds.xform(locator, translation=point, worldSpace=True)
        locators.append(locator)
    
    cmds.select(clear=True)
    print(f"{n} locators créés sur la courbe : {locators}")

# Exemple d'utilisation
N = 5  # Définir le nombre de locators
create_locators_on_curve(N)
