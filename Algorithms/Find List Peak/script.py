peakList = [1,5,2,8,9,6,3,7,10,4]
peakListLength = len(peakList)
maxValue = 0

# if(index==0) then check to right only
# if(index==length-1) then check to left only
# else (check your left and right) if you are greater than you are peak
#print("Number at index {}: {}".format(index+1, num))

for index, num in enumerate(peakList):
  if(index==0):
    if(peakList[index] > peakList[index+1]):
      if(peakList[index] > maxValue):
        maxValue = peakList[index]
  
  elif(index == peakListLength-1):
    if(peakList[index] > peakList[index-1]):
      if(peakList[index] > maxValue):
        maxValue = peakList[index]
        
  else:
    if(peakList[index] > peakList[index-1] and peakList[index] > peakList[index+1]):
      if(peakList[index] > maxValue):
        maxValue = peakList[index]

print(maxValue)