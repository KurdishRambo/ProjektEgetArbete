# See https://docs.python.org/3/library/turtle.html#special-turtle-methods.

#Importerar programmeringspråket Turtle
import turtle

#Får upp själva canvas bilden där mitt spel ska utföras och lägger min tittle och färg.
Turtle = turtle.Screen()
Turtle.title("Alvin Ertas")
Turtle.title("Alvins cookie clicker")
Turtle.bgcolor("Light blue")

# Registerar min cookie på spelet så den syns
Turtle.register_shape("cookie.gif")
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)


# Man börjar med 0 clicks
clicks = 0

#Detta gör så att själva klick mättaren där det står hur många klicks man gjort redigeras till mitten av skärmen och gör den till svart färg.
#Gör penup så att det inte dras en linje och flyttar texten till mitten och skriver på skärmen det som vi vill ha.
# Skriver ut Clicks i storlek 32 och anordnar det i mitten i typesnitt Times New Roman.
pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 250)
pen. write(f"Clicks: {clicks}", align="center", font=("Times New Roman", 32, "normal"))


points = turtle.Turtle()
points.hideturtle()
points.color()
points.penup()
points.goto(280,150)
points. write("50 clicks = 3x", font=("Times New Roman", 20, "normal"))

#Skriver ut och placerar info om vad som händer ifall du kommer till visst antal clicks.
points = turtle.Turtle()
points.hideturtle()
points.color()
points.penup()
points.goto(280,100)
points. write("100 clicks = 5x", font=("Times New Roman", 20, "normal"))

points = turtle.Turtle()
points.hideturtle()
points.color()
points.penup()
points.goto(280,50)
points. write("200 clicks = 7x", font=("Times New Roman", 20, "normal"))

#Gör en funktion som tar två argument x och y som är kopplat till oneclicked metoden.
#Har min clicks + 1 så att man börjar med 1 click = 1 poäng
#Gör if satser så att efter 50 clicks så får man + 2 clicks utöver den befinliga + 1. Alltså + 2 blir helt enkelt + 3 clicks. Sedan ytterligare + 2 clicks efter 100 clicks.
# Och sedan sista bonus click som ligger på 200 click.
#Har min pen clear för annars så hamnar varje nytt click på varandra i click mättaren.
# Använder penwrite så att funktionen hamnar i clickmätren och att den ej ska försvinna efter ja klickat.

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Times New Roman", 32, "normal"))
    if clicks >= (50):
        clicks += 2
        if clicks >= (100):
            clicks += 2
            if clicks >= (200):
                clicks += 2




cookie.onclick(clicked)

#Gör så att spelet inte stängs av direkt.
turtle.mainloop()
