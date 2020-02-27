#Family name: Prabh Simran Singh Badwal
# Student number: 300057572
# Course: IT1 1120[F]
# Assignment Number 4 Part 2


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        self == other if they have the same coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In the case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    def __init__(self, b_point, t_point, color):
        '''(Rectangle, Point, Point, str)->None'''
        self.b_point=b_point
        self.t_point=t_point
        self.color=color
        
    def get_bottom_left(self):
        '''(Rectangle)->Point'''
        return self.b_point
    
    def get_top_right(self):
        '''(Rectangle)->Point'''
        return self.t_point
    
    def get_color(self):
        '''(Rectangle)->str'''
        return self.color
    
    def reset_color(self,newcolor):
        '''(Rectangle,str)->None'''
        self.color=newcolor

    def get_perimeter(self):
        '''(Rectangle)->number'''
        return 2*(self.t_point.x-self.b_point.x) + 2*(self.t_point.y-self.b_point.y)

    def get_area(self):
        '''(Rectangle)->number'''
        return (self.t_point.x-self.b_point.x)*(self.t_point.y-self.b_point.y)

    def move(self, dx,dy):
        '''(Rectangle,number,number)->None'''
        self.b_point.move(dx,dy)
        self.t_point.move(dx,dy)

    def intersects(self,other):
        '''(Rectangle,Rectangle)->bool'''
        if self.t_point.x < other.b_point.x or other.t_point.x < self.b_point.x:
            return False
        elif self.t_point.y < other.b_point.y or other.t_point.y < self.b_point.y:
            return False
        else:
            return True

    def contains(self,x,y):
        '''(Rectangle,number,number)->bool'''
        return (self.b_point.x  <= x) and (x <= self.t_point.x) and (self.b_point.y <= y) and (y <= self.t_point.y) 
        

    def __eq__(self,other):
        '''(Rectangle,Rectangle)->bool'''
        return self.b_point==other.b_point and self.t_point==other.t_point and self.color==other.color

    def __repr__(self):
        '''(Rectangle)->str'''
        return 'Rectangle('+str(self.b_point)+","+str(self.t_point)+","+'\''+self.color+'\')'


    def __str__(self):
        '''(Rectangle)->str'''
        return 'I am a '+self.color+' rectangle with bottom left corner at '+str(self.b_point.get())+' and top right corner at '+str(self.t_point.get())+'.'

class Canvas:
    def __init__(self):
        '''(Canvas)->None'''
        self.q=[]

    def add_one_rectangle(self,other):
        '''(Canvas, Rectangle)->None'''
        self.q.append(other)

    def count_same_color(self, color):
        '''(Canvas, str)->int'''
        count=0
        for item in self.q:
            if item.color==color:
                count=count+1
        return count

    def total_perimeter(self):
        '''(Canvas)->number'''
        total=0
        for item in self.q:
            total=total+item.get_perimeter()
        return total

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle'''
        minx=[]
        maxx=[]
        miny=[]
        maxy=[]

        for item in self.q:
            minx.append(item.b_point.x)
            maxx.append(item.t_point.x)
            miny.append(item.b_point.y)
            maxy.append(item.t_point.y)

        return Rectangle(Point(min(minx), min(miny)), Point(max(maxx), max(maxy)), "red")

    def common_point(self):
        '''(Canvas)->bool'''
        for i in range(len(self.q)):
            for j in range(i+1, len(self.q)):
                if not( self.q[i].intersects(self.q[j]) ):
                    return False
        return True
        
    def __len__(self):
        '''(Canvas)->int'''
        return len(self.q)

    def __repr__(self):
        '''(Canvas)->str'''
        return 'Canvas('+str(self.q)+')'

