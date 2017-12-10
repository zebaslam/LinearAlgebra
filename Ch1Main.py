from vector.Vector import Vector


def main():
    vec1 = Vector((-.221, 7.437))
    vec2 = Vector((8.813, -1.331, -6.247))
    vec3 = Vector((5.581, -2.136))
    vec4 = Vector((1.996, 3.108, -4.554))
    res = vec4.normalize()
    print(res)


if __name__ == '__main__':
    main()
