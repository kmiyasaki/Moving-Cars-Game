from graphics import *
import time
import random

# car class: used to initalize color, x, y, and unit variables used to
#   generate cars
class Car(Rectangle):
    def __init__(self, win, x, y, unit):

        colorlist = ["green","yellow","red","purple","orange","blue"]
        self.color = random.choice(colorlist)
        
        self.x = x
        self.y = y
        self.unit = unit
        
        self.score = int(unit * 10)
        
        self.p1 = Point((x - unit * 4),(y))
        self.p2 = Point((x + unit * 4),(y + unit * 3))
        self.p3 = Point((x),(y + unit * 4))

        super().__init__(self.p1, self.p2)

        self.drawCar(self.p1, self.p2, self.p3, win)

    # getColor: returns the color of the clicked car                     
    def getColor(self):
        return self.color

    # getScore: returns the score from clicking a car
    def getScore(self):
        return self.score

    # drawCar: draws the tires and roof of each car and defines variables
    #   used to draw cars when they are generated
    def drawCar(self, p1, p2, p3, win):
        self.tire_left = Circle(Point(p1.x+abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        self.tire_left.setFill("black")
        self.tire_left.draw(win)

        self.tire_right = Circle(Point(p2.x-abs(p2.x-p1.x)/4,p1.y),abs(p2.x-p1.x)/8)
        self.tire_right.setFill("black")
        self.tire_right.draw(win)

        Rectangle.setFill(self, self.getColor())
        Rectangle.draw(self, win)

        pp1 = Point(p1.x+abs(p2.x-p1.x)/4, p2.y)
        pp3 = Point(p2.x-3*abs(p2.x-p1.x)/8, p3.y)

        pp2 = Point(p1.x+abs(p2.x-p1.x)*3/4, p2.y)
        pp4 = Point(p1.x+3*abs(p2.x-p1.x)/8, p3.y)
        
        self.roof = Polygon(pp1, pp2, pp3, pp4)
        self.roof.setFill("black")
        self.roof.draw(win)
    # move: moves the car body, tires, and roof
    def move(self, Xdistance):
        Rectangle.move(self, Xdistance, 0)
        self.tire_left.move(Xdistance, 0)
        self.tire_right.move(Xdistance, 0)
        self.roof.move(Xdistance, 0)
        
    # undraw: removes the car from the screen after being clicked
    def undraw(self):
        self.tire_left.undraw()
        self.tire_right.undraw()
        Rectangle.undraw(self)
        self.roof.undraw()

# isClicked: determines whether the user click was on a button or car
def isClicked(pclick,button):

    ll = button.getP1()
    ur = button.getP2()

    # if the click was inside a button, return True
    if ll.getX() < pclick.getX() < ur.getX() and ll.getY() < pclick.getY() < ur.getY():
        return True
    else:
        return False

# draw_buildings: draws buildings based on data from the text file
def draw_buildings(win, p1_x,p1_y,p2_x,p2_y,color):
    shape = Rectangle(Point(p1_x,p1_y),Point(p2_x,p2_y))
    shape.setFill(color)
    shape.draw(win)

def main():
    win = GraphWin("Moving Cars", 800, 600)
    win.setCoords(0, 0, 40, 40)

    # draw background
    bg = Rectangle(Point(0,25), Point(40, 40))
    bg.setFill("light blue")
    bg.draw(win)

    ground = Rectangle(Point(0,6) , Point(40, 24))
    ground.setFill("light grey")
    ground.draw(win)
    temp=4

    # draw ground lines
    while temp<40:
        gnd_lines1= Line(Point(temp,10),Point(temp+4,10))
        gnd_lines1.setWidth(5)
        gnd_lines1.setFill("white")
        gnd_lines2= Line(Point(temp,15),Point(temp+4,15))
        gnd_lines2.setWidth(5)
        gnd_lines2.setFill("white")
        gnd_lines3= Line(Point(temp,20),Point(temp+4,20))
        gnd_lines3.setWidth(5)
        gnd_lines3.setFill("white")
        temp=temp+10
        gnd_lines1.draw(win)
        gnd_lines2.draw(win)
        gnd_lines3.draw(win)

    # draw sun
    sun = Circle(Point(37,38), 1.5)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    # opens input text file
    with open('buildings_input.txt','r') as file:
        # reading each line
        for line in file:
            coordinates=[]
            # reading each word
            for word in line.split():
                # displaying the words
                coordinates.append(word)
            draw_buildings(win,coordinates[0],coordinates[1],coordinates[2],coordinates[3],coordinates[4])

    # draw button for start/pause
    button = Rectangle(Point(2,2), Point(6, 4))
    button.setFill("gray")
    button.draw(win)
    label = Text(Point(4, 3), "Start")
    label.setStyle("bold")
    label.setTextColor("white")
    label.draw(win)

    # draw bottom message
    bottom_message = Text(Point(12, 5), "Please click the Start button to begin")
    bottom_message.setStyle("bold")
    bottom_message.setTextColor("green")
    bottom_message.draw(win)
    car_on_screen_message = Text(Point(15, 27), "")
    car_on_screen_message.setStyle("bold")
    car_on_screen_message.setTextColor("purple")
    car_on_screen_message.draw(win)

    # draw score message
    score_title = Text(Point(15, 3), "Current Score: ")
    score_title.setStyle("bold")
    score_title.setSize(18)
    score_title.setTextColor("blue")
    score_title.draw(win)
    score_message = Text(Point(21, 3), "0")
    score_message.setStyle("bold")
    score_message.setSize(18)
    score_message.setTextColor("blue")
    score_message.draw(win)

    # draw clicked color message
    clicked_colors_message = Text(Point(29, 5), "")
    clicked_colors_message.setStyle("bold")
    clicked_colors_message.setTextColor("black")
    clicked_colors_message.draw(win)

    # creates exit background, message, and buttons for pause screen
    exit_bg = Rectangle(Point(10,5), Point(30, 20))
    exit_bg.setFill("light gray")
    exit_message = Text(Point(20, 15), "Click Exit to stop \n or Resume to continue")
    exit_message.setSize(18)
    exit_message.setStyle("bold")
    exit_message.setTextColor("red")
    confirm_button = Rectangle(Point(13, 7), Point(17, 9))
    confirm_button.setFill("gray")
    confirm_label = Text(Point(15, 8), "Exit")
    confirm_label.setStyle("bold")
    confirm_label.setTextColor("white")
    go_back_button = Rectangle(Point(23, 7), Point(27, 9))
    go_back_button.setFill("gray")
    go_back_label = Text(Point(25, 8), "Resume")
    go_back_label.setStyle("bold")
    go_back_label.setTextColor("white")

    # draws clicked color title and box
    mylabel = Text(Point(26,3),"Clicked Color:")
    mylabel.setStyle("bold")
    mylabel.draw(win)
    myrectangle = Rectangle(Point(29,2),Point(31,4))
    myrectangle.draw(win)

    # defining variables for infinite loop
    pixel_per_second = 10
    refresh_sec = 0.05
    gameState = 0
    total_score = 0
    car_list = []

    # clicked_colors: dictionary to score color and amount of cars clicked
    clicked_colors = {}
    
    start_time1 = 0
    start_time2 = 0
    exit_bg_drawn = False

    # infinite loop
    while True:
        pClick = win.checkMouse()

        # INITIAL STATE
        if gameState == 0:
            time.sleep(0.1)

            # user clicks start button
            if pClick != None:
                if isClicked(pClick, button):
                    gameState = 1
                    bottom_message.setText("Click a moving car or Pause to stop")

        # START STATE           
        elif gameState == 1:
            label.setText("Pause")

            # if a click is detected   
            if pClick != None:

                # user clicks pause
                if isClicked(pClick, button):
                    gameState = 2

                # game starts
                for car in car_list:

                    # if a car is clicked
                    if isClicked(pClick, car):

                        # score
                        car.getScore()
                        total_score = total_score + int(100*(1/car.score))
                        score_message.setText(str(total_score))

                        # dictionary and clicked color box
                        car.getColor()
                        myrectangle.setFill(car.color)
                        count = clicked_colors.get(car.getColor(), 0) + 1
                        clicked_colors.update({car.color:count})

                        clrmsg = []
                        comma = ", "
                        space = " "

                        # adds color and value from dictionary to clrmsg
                        #   list to display in clicked_colors_message
                        for key, value in clicked_colors.items():
                            clrmsg.append(key)
                            clrmsg.append(space)
                            clrmsg.append(value)
                            clrmsg.append(comma)

                        # does not add a comma if only one color has been
                        #   clicked
                        if len(clrmsg) > 2:
                            clrmsg.pop()

                        clrmsgfinal = "".join([str(v) for v in clrmsg])
                        clicked_colors_message.setText(clrmsgfinal)

                        # undraws car if clicked
                        car.undraw()
                
                    
            else:       

                # car generation
                current_time = time.time()
                if (current_time - start_time1) >= 0.2:

                    # define x, y, and unit to generate different
                    #   sized cars
                    x = (random.random() - 0.5) + 4
                    y = random.uniform(7, 23)
                    unit = random.random() * 0.6 + 0.4
                        
                    car = Car(win, x, y, unit)
                    car_list.append(car)

                    start_time1 = current_time + 1

                # moving the cars
                if current_time - start_time2 >= refresh_sec:
                    for car in car_list:
                        car.move(pixel_per_second * refresh_sec)

                        # check if a car reaches edge of screen
                        check = car.p2.getX()
                        if check > 800:
                            car.undraw()
                            car.remove(car_list)
                        start_time2 = current_time     

        # PAUSE STATE
        elif gameState == 2:
            time.sleep(0.1)
            
            # draws exit background, text, and buttons
            if exit_bg_drawn == False:
                exit_bg.draw(win)
                exit_message.draw(win)
                confirm_button.draw(win)
                confirm_label.draw(win)
                go_back_button.draw(win)
                go_back_label.draw(win)
                exit_bg_drawn = True

            # if a click is detected
            if pClick != None:

                # user clicks exit: closes program
                if isClicked(pClick, confirm_button):
                    win.close()
                    break

                # user clicks go back: undraws exit background, text,
                #   and buttons
                elif isClicked(pClick, go_back_button):
                    exit_bg_drawn = False
                    exit_bg.undraw()
                    exit_message.undraw()
                    confirm_button.undraw()
                    confirm_label.undraw()
                    go_back_button.undraw()
                    go_back_label.undraw()

                    gameState = 1


if __name__ == '__main__':
    main()
