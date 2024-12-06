from vmd import*
import os

# Read the VMD
fpath = "test.vmd"
if not os.path.exists(fpath):
    print("File does not exist")
else:
    with open(fpath, "rb") as file:
        # Header
        vmd_header = VMD_HEADER(
            VmdHeader=vmdread(file, 30, "30s"),
            VmdModelName=vmdread(file, 20, "20s")
            )
        print(vmd_header.VmdHeader)
        print("Model : ", vmd_header.VmdModelName)

        # Motion Data Count
        vmd_motion_count = VMD_MOTION_COUNT(Count=vmdread(file, 4, "I"))
        print("Motion Count :", vmd_motion_count.Count)

        # Motion Data
        for _count in range(vmd_motion_count.Count):
            vmd_motion = VMD_MOTION(
                BoneName=vmdread(file, 15, "15s"),
                FrameNo=vmdread(file, 4, "I"),
                Location=vmdread(file, 12, "3f"),
                Rotation=vmdread(file, 16, "4f"),
                Interpolation=vmdread(file, 64, "64B")
            )

            print(
                vmd_motion.BoneName, " ",
                vmd_motion.FrameNo, "\n",
                vmd_motion.Location[0], " ",
                vmd_motion.Location[1], " ",
                vmd_motion.Location[2], "\n",
                vmd_motion.Rotation[0], " ",
                vmd_motion.Rotation[1], " ",
                vmd_motion.Rotation[2], "\n",
                # vmd_motion.Interpolation,
            )

        print("\n")

        # Facial Animation Data Count
        vmd_skin_count = VMD_SKIN_COUNT(Count=vmdread(file, 4, "I"))
        print("Skin Count : ", vmd_skin_count.Count)

        # Facial Animation Data
        for _count in range(vmd_skin_count.Count):
            vmd_skin = VMD_SKIN(
                SkinName=vmdread(file, 15, "15s"),
                FrameNo=vmdread(file, 4, "I"),
                Weight=vmdread(file, 4, "f")
            )

            print(
                vmd_skin.SkinName, " ",
                vmd_skin.FrameNo, " ",
                vmd_skin.Weight
            )

# Cloose the vmd
file.close()