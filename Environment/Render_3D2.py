import harfang as hg

def render_3d(approaches, exits):
    hg.InputInit()
    hg.WindowSystemInit()

    res_x, res_y = 1024, 1024
    wnd = hg.RenderInit('Intersection 3D', res_x, res_y, hg.RF_VSync | hg.RF_MSAA4X)

    hg.AddAssetsFolder('resources_compiled')

    pipeline = hg.CreateForwardPipeline()
    res = hg.PipelineResources()

    scene = hg.Scene()


    frame_buffer = hg.CreateFrameBuffer(512, 512, hg.TF_RGBA32F, hg.TF_D24, 4, 'framebuffer')  # 4x MSAA
    color = hg.GetColorTexture(frame_buffer)

    # Create sphere in center
    sphere = hg.CreateSphere(0.5, 32, 32)

    # create a new node to attach the sphere to
    node = hg.Node()

    # attach the sphere to the node
    node.AddComponent(hg.Sphere(sphere))

    # set the position of the node
    node.SetPosition(hg.Vector3(0, 0, 0))

    # add the node to the scene
    scn = hg.Scene()
    scn.AddNode(node)

    # render the scene
    hg.RenderScene(scn)

    while True:
        hg.frame()
        hg.UpdateWindow(wnd)