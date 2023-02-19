#######################
# Uygulama - Mülakat Sorusu
#######################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

# English version !!
# Put the students in the double index into a list.
# Take the students in one index to another list.
# But these two lists return as a single list.

students = ["John", "Mark", "Venessa", "Mariam"]


def studentdivider(liste):
    A = [[], []]
    for index, a in enumerate(liste):
        if index % 2 == 0:
            A[0].append(a)
        else:
            A[1].append(a)
    print(A)
    return A


studentdivider(students)
