h = float(input('wall height: '))
w = float(input('wall width: '))

a = h*w
ink = a/2

print("the dimension of your wall is {}x{} and its area is {}m²." .format(h, w, a))
print("you're gonna need {:.1f}l of ink to paint it." .format(ink))