import turtle

# Funktion för att generera L-system-strängen
def generera_lsystem(iters, axiom, regler):
    start = axiom
    for _ in range(iters):
        nytt_string = ""
        for tecken in start:
            nytt_string += regler.get(tecken, tecken)
        start = nytt_string
    return start

# Funktion för att rita L-systemet med turtle
def rita_lsystem(t, instruktioner, längd, vinkel):
    stack = []
    for kommand in instruktioner:
        if kommand == "F":
            t.forward(längd)  # Rita framåt
        elif kommand == "+":
            t.right(vinkel)   # Vrid höger
        elif kommand == "-":
            t.left(vinkel)    # Vrid vänster
        elif kommand == "[":
            stack.append((t.position(), t.heading()))  # Spara position och riktning
        elif kommand == "]":
            position, riktning = stack.pop()  # Återställ position och riktning
            t.penup()
            t.goto(position)
            t.setheading(riktning)
            t.pendown()

# Regler för ett enkelt L-system (t.ex. en variant av en fraktalväxt)
regler = {
    "F": "FF",  # Varje "F" ersätts med två "F"
    "X": "F-[[X]+X]+F[+FX]-X"  # X används för rekursiva grenmönster
}

# Axiomet, dvs startsträngen
axiom = "X"

# Parametrar
iters = 5        # Antal iterationer
längd = 5        # Längd på varje linje
vinkel = 25      # Vinkel för grenarna

# Skapa L-system-strängen
lsystem_str = generera_lsystem(iters, axiom, regler)

# Skapa turtle-fönster
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")

# Rita L-systemet
rita_lsystem(t, lsystem_str, längd, vinkel)

# Stäng fönstret vid klick
turtle.exitonclick()
