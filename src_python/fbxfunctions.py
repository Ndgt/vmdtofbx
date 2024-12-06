from fbx import*

def CreateSquare(mesh: FbxMesh) -> None:
    # Define the vertices of a square
    vertices = (
        FbxVector4(-50, -50, 0),
        FbxVector4( 50, -50, 0),
        FbxVector4( 50,  50, 0),
        FbxVector4(-50,  50, 0),
    )

    mesh.InitControlPoints(4)
    for i in range(4):
        mesh.SetControlPointAt(vertices[i], i)
    
    mesh.BeginPolygon()
    for i in range(4):
        mesh.AddPolygon(i)
    
    mesh.EndPolygon()


def CreateBlendShapeTarget(baseMesh: FbxMesh, name: str) -> FbxShape:
    # Create a shape for the blend target
    blendShapeTarget = FbxShape.Create(baseMesh, name)
    blendShapeTarget.InitControlPoints(4)

    # set control points of FbxShape that will not move
    for i in range(4):
        blendShapeTarget.SetControlPointAt(baseMesh.GetControlPointAt(i), i)

    return blendShapeTarget


def AddBlendShapes(mesh: FbxMesh) -> None:
    # Create the blend shape deformer
    blendShape = FbxBlendShape.Create(mesh, "SourceFace_BlendShape")
    mesh.AddDeformer(blendShape)

    # Create 5 different blend shape channels
    shapekeynames = ("a", "i", "u", "e", "o")

    for i in range(len(shapekeynames)):
        channelName = "BlendShapeChannel_" + str(i+1)
        blendShapeChannel = FbxBlendShapeChannel.Create(blendShape, channelName)
        blendShape.AddBlendShapeChannel(blendShapeChannel)

        # Create a blend shape target and add it to the channel
        shapeName = shapekeynames[i]
        blendShapeTarget = CreateBlendShapeTarget(mesh, shapeName)
        blendShapeChannel.AddTargetShape(blendShapeTarget)
