def line():
  A = float(input ("Ingrese el coeficiente A:"))
    B = float(input ("Ingrese el coeficiente B:"))
    X1 = float(input ("Ingrese el coeficiente X1:"))
    X2 = float(input ("Ingrese el coeficiente X2:"))

    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente A de su ecuación de la recta es: {B}")
    print(f"El coeficiente A de su ecuación de la recta es: {X1}")
    print(f"El coeficiente A de su ecuación de la recta es: {X2}")

    print("Para la siguiente ecuación:")
    print(float(f"Y = {A}X + {B}"))

    Y1 = A*X1 + B
    Y2 = A*X2 + B

    print("Dados los siguientes puntos:")
    print((f"{X1}, {Y1}"))
    print((f"{X2}, {Y2}"))

    distancia = math.sqart((X2 - X1)**2 + (Y2 - Y1)**2)
    print(f"La distancia entre ellos es: {distancia}")
