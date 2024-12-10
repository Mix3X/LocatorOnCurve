
# Maya Python Script - Create Equidistant Locators on Curve

This Python script for Autodesk Maya allows you to create equidistant locators along a selected NURBS curve. The number of locators is defined by the user and they are placed evenly between the first and the last point of the curve.

# Features
Creates locators on a selected NURBS curve.
Locators are placed equidistantly between the first and the last point of the curve.
The number of locators (N) is user-definable.
Compatible with NURBS curves created in Maya.

# Usage
Select a NURBS curve in your scene. Make sure that the curve is a NURBS curve (you can verify this by selecting the curve and checking the Outliner or Attribute Editor).
Define the number of locators you want to create by modifying the N variable in the script.
Run the script.
Locators will be created equidistantly between the first and the last point of the selected curve.

# Example Usage
python
Copy code
# Set the number of locators
N = 5

# Create the locators on the selected curve
create_locators_on_curve(N)
This will create 5 locators evenly distributed along the curve.

# Parameters
N: The number of locators to create. It must be a positive integer.
By default, N = 5, but you can adjust this value as needed.

# Limitations
The script only works with NURBS curves.
The number of locators (N) must be 2 or greater; otherwise, the script won't work correctly.
The curve must be selected before running the scrip
