import cv2 as cv 

def getBoundaryPts (rows, colls, img): 
    pts = []
    
    for x in range(colls): 
        minY = rows 
        maxY = 0
        isPastFirstPt = False 
        for y in range(rows):
            if img[y][x] < 200:
                if not(isPastFirstPt): 
                    minY =y
                isPastFirstPt = True 
                if maxY < img[y][x]: 
                    maxY = y
        
        pts.append(str(rows - minY))
        pts.append(str(rows - maxY))
        
    return pts
             
    

graph = cv.imread("sample.png", 0)
rows, colls = graph.shape

boundaryPts = getBoundaryPts(rows, colls, graph)

with open("extractedData.wav", "w") as csvf: 
    csvf.writelines(",\n".join(boundaryPts))
    csvf.close()