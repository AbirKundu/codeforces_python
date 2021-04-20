no_of_polyhedrons = int(input())
polyhedrons = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
}
total_no_faces = 0
for i in range(no_of_polyhedrons):
    shape = input()
    total_no_faces += polyhedrons[shape]

print(total_no_faces)
