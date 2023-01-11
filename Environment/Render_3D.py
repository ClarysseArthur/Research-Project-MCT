import HarfangHighLevel as hl
import harfang as hg

def render_3d(approaches, exits):
    hl.Init(1280, 720)
    hl.AddFpsCamera(-20, 40, -20)
    lanes_length = []

    rnd = hg_renderer.CreateRenderer()

    for i, approach in enumerate(approaches):
        lanes_length.append(approach.get_length())
    
    for i, exit in enumerate(exits):
        lanes_length[i] += exit.get_length()

    print(lanes_length)

    for i, x in enumerate(lanes_length):
        offset = 0
        if x + 1 < len(lanes_length):
            offset = lanes_length[i + 1] * 3.5
        else:
            offset = lanes_length[0] * 3.5

        if i == 0:
            xyz1 = [0, 0, 15 + offset]
            xyz2 = [[-1.75, 0, 15 + offset], [1.75, 0, 15 + offset]]
            xyz3 = [[-3.5, 0, 15 + offset], [0, 0, 15 + offset], [3.5, 0, 15 + offset]]
            xyz4 = [[-5.25, 0, 15 + offset], [-1.75, 0, 15 + offset], [1.75, 0, 15 + offset], [5.25, 0, 15 + offset]]
            xyz5 = [[-7, 0, 15 + offset], [-3.5, 0, 15 + offset], [0, 0, 15 + offset], [3.5, 0, 15 + offset], [7, 0, 15 + offset]]
            xyz6 = [[-8.75, 0, 15 + offset], [-5.25, 0, 15 + offset], [-1.75, 0, 15 + offset], [1.75, 0, 15 + offset], [5.25, 0, 15 + offset], [8.75, 0, 15 + offset]]
            xyz_dim = [3.5, 0.5, 30]
        elif i == 1:
            xyz1 = [15 + offset, 0, 0]
            xyz2 = [[15 + offset, 0, -1.75], [15 + offset, 0, 1.75]]
            xyz3 = [[15 + offset, 0, -3.5], [15 + offset, 0, 0], [15 + offset, 0, 3.5]]
            xyz4 = [[15 + offset, 0, -5.25], [15 + offset, 0, -1.75], [15 + offset, 0, 1.75], [15 + offset, 0, 5.25]]
            xyz5 = [[15 + offset, 0, -7], [15 + offset, 0, -3.5], [15 + offset, 0, 0], [15 + offset, 0, 3.5], [15 + offset, 0, 7]]
            xyz6 = [[15 + offset, 0, -8.75], [15 + offset, 0, -5.25], [15 + offset, 0, -1.75], [15 + offset, 0, 1.75], [15 + offset, 0, 5.25], [15 + offset, 0, 8.75]]
            xyz_dim = [30, 0.5, 3.5]
        elif i == 2:
            xyz1 = [0, 0, -15 - offset]
            xyz2 = [[-1.75, 0, -15 - offset], [1.75, 0, -15 - offset]]
            xyz3 = [[-3.5, 0, -15 - offset], [0, 0, -15 - offset], [3.5, 0, -15 - offset]]
            xyz4 = [[-5.25, 0, -15 - offset], [-1.75, 0, -15 - offset], [1.75, 0, -15 - offset], [5.25, 0, -15 - offset]]
            xyz5 = [[-7, 0, -15 - offset], [-3.5, 0, -15 - offset], [0, 0, -15 - offset], [3.5, 0, -15 - offset], [7, 0, -15 - offset]]
            xyz6 = [[-8.75, 0, -15 - offset], [-5.25, 0, -15 - offset], [-1.75, 0, -15 - offset], [1.75, 0, -15 - offset], [5.25, 0, -15 - offset], [8.75, 0, -15 - offset]]
            xyz_dim = [3.5, 0.5, 30]
        elif i == 3:
            xyz1 = [-15 - offset, 0, 0]
            xyz2 = [[-15 - offset, 0, -1.75], [-15 - offset, 0, 1.75]]
            xyz3 = [[-15 - offset, 0, -3.5], [-15 - offset, 0, 0], [-15 - offset, 0, 3.5]]
            xyz4 = [[-15 - offset, 0, -5.25], [-15 - offset, 0, -1.75], [-15 - offset, 0, 1.75], [-15 - offset, 0, 5.25]]
            xyz5 = [[-15 - offset, 0, -7], [-15 - offset, 0, -3.5], [-15 - offset, 0, 0], [-15 - offset, 0, 3.5], [-15 - offset, 0, 7]]
            xyz6 = [[-15 - offset, 0, -8.75], [-15 - offset, 0, -5.25], [-15 - offset, 0, -1.75], [-15 - offset, 0, 1.75], [-15 - offset, 0, 5.25], [-15 - offset, 0, 8.75]]
            xyz_dim = [30, 0.5, 3.5]

        if x == 1:
            hl.AddPhysicBox(xyz1[0], xyz1[1], xyz1[2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red)

        elif x == 2:
            hl.AddPhysicBox(xyz2[0][0], xyz2[0][1], xyz2[0][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red)
            hl.AddPhysicBox(xyz2[1][0], xyz2[1][1], xyz2[1][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Blue)
        elif x == 3:
            material = hl.Material()

            texture = rnd.CreateTexture("C:\\Users\\arthu\\Desktop\\MCT\\04 Reasearch Project\\Research-Project-MCT\\Environment\\testtexture.png")

            material.SetDiffuseMap(texture)

            box4 = hl.AddPhysicBox(xyz3[0][0], xyz3[0][1], xyz3[0][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red, material=material)
            box5 = hl.AddPhysicBox(xyz3[1][0], xyz3[1][1], xyz3[1][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Blue)
            box6 = hl.AddPhysicBox(xyz3[2][0], xyz3[2][1], xyz3[2][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Green)

            
        elif x == 4:
            hl.AddPhysicBox(xyz4[0][0], xyz4[0][1], xyz4[0][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red)
            hl.AddPhysicBox(xyz4[1][0], xyz4[1][1], xyz4[1][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Blue)
            hl.AddPhysicBox(xyz4[2][0], xyz4[2][1], xyz4[2][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Green)
            hl.AddPhysicBox(xyz4[3][0], xyz4[3][1], xyz4[3][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Yellow)
        elif x == 5:
            hl.AddPhysicBox(xyz5[0][0], xyz5[0][1], xyz5[0][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red)
            hl.AddPhysicBox(xyz5[1][0], xyz5[1][1], xyz5[1][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Blue)
            hl.AddPhysicBox(xyz5[2][0], xyz5[2][1], xyz5[2][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Green)
            hl.AddPhysicBox(xyz5[3][0], xyz5[3][1], xyz5[3][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Yellow)
            hl.AddPhysicBox(xyz5[4][0], xyz5[4][1], xyz5[4][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.White)
        elif x == 6:
            hl.AddPhysicBox(xyz6[0][0], xyz6[0][1], xyz6[0][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Red)
            hl.AddPhysicBox(xyz6[1][0], xyz6[1][1], xyz6[1][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Blue)
            hl.AddPhysicBox(xyz6[2][0], xyz6[2][1], xyz6[2][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Green)
            hl.AddPhysicBox(xyz6[3][0], xyz6[3][1], xyz6[3][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Yellow)
            hl.AddPhysicBox(xyz6[4][0], xyz6[4][1], xyz6[4][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.White)
            hl.AddPhysicBox(xyz6[5][0], xyz6[5][1], xyz6[5][2], size_x=xyz_dim[0], size_y=xyz_dim[1], size_z=xyz_dim[2], color=hl.Color.Black)


    hl.AddPhysicSphere(0, 0, 0, 0.5, color=hl.Color.Red)

    while not hl.UpdateDraw():
        pass