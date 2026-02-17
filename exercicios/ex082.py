from direct.showbase.ShowBase import ShowBase
from panda3d.core import GeomvertexFormat, GeomVertexData, Geom, GeomNode, GeomTriangles
from panda3d.core import GeomVertexWritter, Vec3, AmbientLight, DirecionalLight
from panda3d.core import LVector3
from direct.task import Task

def make_cube(size: float = 1.0) -> GeomNode:
    s = size / 2.0
    verts = [
        (-s, -s, -s), (s, -s, -s), (s, s, -s), (-s, s, -s),
        (-s, -s, s), (s, -s, s), (s, s, s), (-s, s, s)
    ]

    faces = [
        (0, 1, 2), (0,2,3),
        (4,6,5), (4,7,6),
        (0, 4, 5), (0, 5, 1),
        (1, 5, 6), (1, 6, 2),
        (2, 6, 7), (2,7, 3),
        (3,7, 4), (3, 4, 0)
    ]
    
    fmt = GeomvertexFormat.get_v3n3()
    vdata = GeomVertexData('cube', fmt, Geom.UHStatic)

    vw = GeomVertexWritter(vdata, 'vertex')
    nw = GeomVertexWritter(vdata, 'normal')
    for (a, b, c) in faces:
        va, vb, vc = Vec3(*verts[a]), Vec3(*verts[b]), Vec3(*verts[c])
        normal = (vb - va).cross(vc - va)
        normal.normalize()

        for v in (va, vb, vc):
            vw.addData3(v)
            nw.addData3(normal)

    tris = GeomTriangles(Geom.UHStatic)

    for i in range(0, len(faces) * 3, 3):
        tris.addVertices(i, i + 1, i + 2)
    tris.closePrimitive()

    geom = Geom(vdata)
    geom.AddPrimitive(tris)
    return GeomNode

class app(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()

        self.camera.setPos(0, -6, 2)
        self.camera.lookAt(0, 0, 0)

        ambient = AmbientLight("ambient")
        ambient.setColor((0.25, 0.9, 0.9, 1))
        dlnp = self.render.attachNewNode(DirecionalLight)
        dlnp.SetHpr(45, - 45, 0)
        self.render.setlight(dlnp)

        cube_node = make_cube(1.5)
        self.cube = self.render.attachNewNode(cube_node)