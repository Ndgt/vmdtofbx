from vmd import*
from fbxfunctions import*

# Configure New Scene
lSdkManager = FbxManager.Create()
ios = FbxIOSettings.Create(lSdkManager, "Export") # IOSN_EXPORT
lSdkManager.SetIOSettings(ios)
lScene = FbxScene.Create(lSdkManager, "New Scene")

# Create the mesh
mesh = FbxMesh.Create(lScene, "SquareMesh")
CreateSquare(mesh)

# Add the blend shapes
AddBlendShapes(mesh)

# Add the mesh to a node in the scene
meshnode = FbxNode.Create(lScene, "SourceFace")
meshnode.SetNodeAttribute(mesh)
lScene.GetRootNode().AddChild(meshnode)

# Prepare for export
fbxoutputpath = "C:/fbx_python_test/test.fbx"
lExporter = FbxExporter.Create(lSdkManager, "")
lExporter.Initialize(fbxoutputpath, -1, ios)

# Export the Scene
if lExporter.Export(lScene):
    print("The test fbx file successfully exported.")
else:
    print("Failed to export the test fbx file...")

# Cleanup
lExporter.Destroy()
lSdkManager.Destroy()