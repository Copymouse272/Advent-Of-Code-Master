#open file
giftlist = open('input.txt', 'r')

totalsurface = 0

for gifts in giftlist:

    print(gifts)
    length, width, height = gifts.split('x')
    l = int(length)
    w = int(width)
    h = int(height)
    area1 = l*w
    area2 = w*h
    area3 = h*l
    slack = min(area1, area2, area3)
    surfacearea = (2*area1 + 2*area2 + 2*area3 + slack)
    totalsurface += surfacearea

print("The total surface area in the gift-list is:", totalsurface, "Square Feet.")




