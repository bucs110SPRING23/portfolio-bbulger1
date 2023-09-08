from rectangle import Rectangle
from surface import Surface

def main():
    r = Rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.height, r.width) == (10, 10, 10, 10))
    r = Rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (-1, 1, 1, 1))
    r = Rectangle(1, -5, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1, -5, 1, 1))
    r = Rectangle(1, 1, 1, -1000)
    assert((r.x, r.y, r.height, r.width) == (1, 1, 1, -1000))

    s = Surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10, 10, 10, 10))
    srect = s.getRect()
    assert((srect.x, s.getRect().y, srect.height, srect.width) == (10, 10, 10, 10))
    assert s.image
    print("Test Complete!")

main()