import gridlabd

try:
    gridlabd.command("test_house.glm")
    gridlabd.start("wait")
except:
    raise


print ("Hector Run")