from pysketcherMaster.pysketcher import MatplotlibDraw as mpltd
from pysketcherMaster.pysketcher import shapes as shps
import math

width = 10
height = 10
divisible = 2

# set up coordinate plane for project
shps.drawing_tool.set_coordinate_system(xmin = -3, xmax = width, ymin = 0, ymax = height)
shps.drawing_tool.set_linecolor('black')
shps.drawing_tool.set_linewidth(1)

# creating wall
wall = shps.Rectangle(lower_left_corner=(-0.25,0), width = 0.25, height = height)

# creating pin
thickness = 0.5
p1 = shps.point(0, height/divisible - thickness)
p2 = shps.point(0, height/divisible + thickness)
p3 = shps.point(thickness, height/divisible)
pin = shps.Triangle(p1,p2,p3)
pin.set_filled_curves('black')

# creating bar
p4 = (0, height/divisible - 0.25*thickness)
barWidth = 4
barHeight = 0.5*thickness
bar = shps.Rectangle(lower_left_corner=(p4), width=barWidth, height=barHeight)

# creating tension cable
distanceFromTop = 0
p5 = shps.point(0, height - distanceFromTop)
distanceTensionEndBar = 0
p6 = shps.point(barWidth - distanceTensionEndBar, height/divisible + 0.25*thickness) 
cable = shps.Line(p5,p6)

# creating load
distanceLoadEndBar = 3
dimensionLoad = 1.5
p7 = shps.point(barWidth - distanceLoadEndBar, height/divisible - 0.25*thickness)
p8 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness)
loadRope = shps.Line(p7,p8)

p9 = shps.point(barWidth - distanceLoadEndBar - 0.5*dimensionLoad, height/divisible - thickness - dimensionLoad)
load = shps.Rectangle(lower_left_corner=(p9), width=dimensionLoad, height=dimensionLoad)

# creating dimensions
dimensionSpacing = 1
tickMarks = 0.25

# tension dimension
tenDim1 = shps.point(-dimensionSpacing, height/divisible + 0.25*thickness)
tenDim2 = shps.point(-dimensionSpacing, height - distanceFromTop)
tensionDimension = shps.Line(tenDim1,tenDim2)

tenTick1 = shps.point(-dimensionSpacing - tickMarks, height/divisible + 0.25*thickness)
tenTick2 = shps.point(-dimensionSpacing + tickMarks, height/divisible + 0.25*thickness)
tensionTick1 = shps.Line(tenTick1,tenTick2)

tenTick3 = shps.point(-dimensionSpacing - tickMarks, height - distanceFromTop)
tenTick4 = shps.point(-dimensionSpacing + tickMarks, height - distanceFromTop)
tensionTick2 = shps.Line(tenTick3,tenTick4)

# bar dimension, wall to load
barDim1 = shps.point(0, height/divisible - thickness - dimensionLoad - dimensionSpacing)
barDim2 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing)
barDimension1 = shps.Line(barDim1, barDim2)

barTick1 = shps.point(0, height/divisible - thickness - dimensionLoad - dimensionSpacing + tickMarks)
barTick2 = shps.point(0, height/divisible - thickness - dimensionLoad - dimensionSpacing - tickMarks)
barTickMark1 = shps.Line(barTick1,barTick2)

barTick3 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing + tickMarks)
barTick4 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing - tickMarks)
barTickMark2 = shps.Line(barTick3,barTick4)

# bar dimension, load to end of bar
barDim3 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing)
barDim4 = shps.point(barWidth, height/divisible - thickness - dimensionLoad - dimensionSpacing)
barDimension2 = shps.Line(barDim3,barDim4)

barTick5 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing + tickMarks)
barTick6 = shps.point(barWidth - distanceLoadEndBar, height/divisible - thickness - dimensionLoad - dimensionSpacing - tickMarks)
barTickMark3 = shps.Line(barTick5, barTick6)

barTick7 = shps.point(barWidth, height/divisible - thickness - dimensionLoad - dimensionSpacing + tickMarks)
barTick8 = shps.point(barWidth, height/divisible - thickness - dimensionLoad - dimensionSpacing - tickMarks)
barTickMark4 = shps.Line(barTick7,barTick8)

# arc dimension between bar and cable
center = shps.point(barWidth - distanceTensionEndBar, height/divisible + 0.25*thickness)
radius = 1.5

# finding distances for opposites and adjacent sides of triangle
def calculateDistance(start,stop):
    shps.is_sequence(start,stop)

    distance = math.sqrt((start[0]-stop[0])**2 + (start[1]-stop[1])**2)
    return distance

# finding points for triangle
topLeftCorner = shps.point(0, height - distanceFromTop)
bottomLeftCorner = shps.point(0, height/divisible + 0.25*thickness)
rightCorner = shps.point(barWidth - distanceTensionEndBar, height/divisible + 0.25*thickness)

opposite = calculateDistance(topLeftCorner,bottomLeftCorner)
adjacent = calculateDistance(bottomLeftCorner,rightCorner)

angle = math.degrees(math.atan(opposite/adjacent))
print(angle)

arcDim = shps.Arc(center, radius, 180, -angle)

# text within dimensions
textSpacing = 0.25

tensionPos = shps.point(-dimensionSpacing - textSpacing, 5)
tensionText = shps.Text('#', tensionPos, alignment='center', fontsize=3, bgcolor='black')

# grouping components into one group
fig = shps.Composition({'wall':wall, 'pin':pin, 'bar':bar, 'cable':cable, 'loadRope':loadRope, 'load':load})

tensionDimensions = shps.Composition({'tensionDim':tensionDimension, 'tensionTick1':tensionTick1, 'tensionTick2':tensionTick2})
barDimensions = shps.Composition({'barDim1':barDimension1, 'barTickMark1':barTickMark1, 'barTickMark2':barTickMark2, 'barDim2':barDimension2, 'barTickMark3':barTickMark3, 'barTickMark4':barTickMark4})

dimensions = shps.Composition({'tensionDimensions':tensionDimensions, 'barDimensions':barDimensions, 'arcDim':arcDim})
dimensions.set_linewidth(3)
dimensions['arcDim'].set_linestyle('dashed')

text = shps.Composition({'tensionText':tensionText})

fullFig = shps.Composition({'fig':fig, 'dimensions':dimensions})

fullFig.draw()

shps.drawing_tool.display()
shps.drawing_tool.savefig('Advanced.png',crop=False)