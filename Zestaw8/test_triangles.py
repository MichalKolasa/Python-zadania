import pytest
from Zestaw6.points import Point
from triangles import Triangle


@pytest.fixture
def triangles():
    return (
        Triangle(0, 0, 3, 0, 1, 2),
        Triangle(1, 1, 4, 2, 2, 5),
        Triangle(-2, 3, 0, 7, 3, 1),
        Triangle(0, 0, 3, 0, 1, 2),  # taki jak pierwszy
    )


@pytest.mark.parametrize("i,expected", [
    (0, "[(0, 0), (3, 0), (1, 2)]"),
    (1, "[(1, 1), (4, 2), (2, 5)]"),
    (2, "[(-2, 3), (0, 7), (3, 1)]"),
])
def test_str(triangles, i, expected):
    assert str(triangles[i]) == expected


@pytest.mark.parametrize("i,expected", [
    (0, "Triangle(0, 0, 3, 0, 1, 2)"),
    (1, "Triangle(1, 1, 4, 2, 2, 5)"),
    (2, "Triangle(-2, 3, 0, 7, 3, 1)"),
])
def test_repr(triangles, i, expected):
    assert repr(triangles[i]) == expected


@pytest.mark.parametrize("i,j,expected", [
    (0, 1, False), (0, 2, False), (2, 1, False),
    (3, 0, True), (3, 1, False), (3, 2, False),
    (3, 3, True), (2, 2, True), (1, 1, True), (0, 0, True),
])
def test_eq(triangles, i, j, expected):
    assert (triangles[i] == triangles[j]) is expected


@pytest.mark.parametrize("i,j,expected", [
    (0, 1, True), (0, 2, True), (2, 1, True),
    (3, 0, False), (3, 1, True), (3, 2, True),
    (3, 3, False), (2, 2, False), (1, 1, False), (0, 0, False),
])
def test_ne(triangles, i, j, expected):
    assert (triangles[i] != triangles[j]) is expected


@pytest.mark.parametrize("i,expected", [
    (0, Point(1.333, 0.667)),
    (1, Point(2.333, 2.667)),
    (2, Point(0.333, 3.667)),
])
def test_center(triangles, i, expected):
    c = triangles[i].center
    assert c.x == pytest.approx(expected.x, abs=1e-3)
    assert c.y == pytest.approx(expected.y, abs=1e-3)


@pytest.mark.parametrize("i,expected", [
    (0, 3), (1, 5.5), (2, 12),
])
def test_area(triangles, i, expected):
    assert triangles[i].area() == expected


@pytest.mark.parametrize("i,dx,dy,expected", [
    (0, 1, 1, Triangle(1, 1, 4, 1, 2, 3)),
    (1, -3, 8, Triangle(-2, 9, 1, 10, -1, 13)),
    (2, -7, 10, Triangle(-9, 13, -7, 17, -4, 11)),
])
def test_move(triangles, i, dx, dy, expected):
    assert triangles[i].move(dx, dy) == expected


@pytest.mark.parametrize("i,expected", [
    (0, (Triangle(0, 0, 1.5, 0.0, 0.5, 1.0),
         Triangle(1.5, 0.0, 3, 0, 2.0, 1.0),
         Triangle(2.0, 1.0, 0.5, 1.0, 1.5, 0.0),
         Triangle(1, 2, 0.5, 1.0, 2.0, 1.0))),
    (1, (Triangle(1, 1, 2.5, 1.5, 1.5, 3.0),
         Triangle(2.5, 1.5, 4, 2, 3.0, 3.5),
         Triangle(3.0, 3.5, 1.5, 3.0, 2.5, 1.5),
         Triangle(2, 5, 1.5, 3.0, 3.0, 3.5))),
    (2, (Triangle(-2, 3, -1.0, 5.0, 0.5, 2.0),
         Triangle(-1.0, 5.0, 0, 7, 1.5, 4.0),
         Triangle(1.5, 4.0, 0.5, 2.0, -1.0, 5.0),
         Triangle(3, 1, 0.5, 2.0, 1.5, 4.0))),
])
def test_make4(triangles, i, expected):
    assert triangles[i].make4() == expected


def test_from_points():
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(1, 2)
    tr = Triangle.from_points((p1, p2, p3))
    assert tr == Triangle(0, 0, 3, 0, 1, 2)


@pytest.mark.parametrize("i,top,left,bottom,right,width,height", [
    (0, 2, 0, 0, 3, 3, 2),
    (1, 5, 1, 1, 4, 3, 4),
    (2, 7, -2, 1, 3, 5, 6),
])
def test_bounding_box(triangles, i, top, left, bottom, right, width, height):
    t = triangles[i]
    assert t.top == top
    assert t.left == left
    assert t.bottom == bottom
    assert t.right == right
    assert t.width == width
    assert t.height == height


@pytest.mark.parametrize("i,expected", [
    (0, Point(0, 2)),
    (1, Point(1, 5)),
    (2, Point(-2, 7)),
])
def test_topleft(triangles, i, expected):
    assert triangles[i].topleft == expected


@pytest.mark.parametrize("i,expected", [
    (0, Point(0, 0)),
    (1, Point(1, 1)),
    (2, Point(-2, 1)),
])
def test_bottomleft(triangles, i, expected):
    assert triangles[i].bottomleft == expected


@pytest.mark.parametrize("i,expected", [
    (0, Point(3, 2)),
    (1, Point(4, 5)),
    (2, Point(3, 7)),
])
def test_topright(triangles, i, expected):
    assert triangles[i].topright == expected


@pytest.mark.parametrize("i,expected", [
    (0, Point(3, 0)),
    (1, Point(4, 1)),
    (2, Point(3, 1)),
])
def test_bottomright(triangles, i, expected):
    assert triangles[i].bottomright == expected


@pytest.mark.parametrize("x1,y1,x2,y2,x3,y3", [
    (0, 0, 1, 1, 2, 2),
])
def test_constructor_exceptions(x1, y1, x2, y2, x3, y3):
    with pytest.raises(ValueError):
        Triangle(x1, y1, x2, y2, x3, y3)


@pytest.mark.parametrize("data,exc", [
    ([Point(0, 0), Point(1, 1)], ValueError),
    ([Point(0, 0), "A", Point(1, 1)], TypeError),
])
def test_from_points_exceptions(data, exc):
    with pytest.raises(exc):
        Triangle.from_points(data)
