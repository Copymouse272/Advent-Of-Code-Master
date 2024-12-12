#open file
giftlist = open('input.txt', 'r')
#gifts = giftlist.readline()
totalribbon = 0

for gifts in giftlist:

    print(gifts)
    length, width, height = gifts.split('x')
    l = int(length)
    w = int(width)
    h = int(height)
    volume = l*w*h
    sides = [l, w, h]
    sides.sort()
    print(sides)
    ribbon1 = sides[0]
    ribbon2 = sides[1]
    pribbon = ribbon1 + ribbon1 + ribbon2 + ribbon2 + volume
    print(pribbon)
    totalribbon += pribbon

print("The total ribbon needed is:", totalribbon, "Feet.")




