def moveTower(height, fromPole, toPole, intermediate):
    if height < 1:
        return 

    moveTower(height-1, fromPole, intermediate, toPole)
    moveDisk(fromPole, toPole)
    moveTower(height-1, intermediate, toPole, fromPole)

def moveDisk(fp, tp):
    print "moving the disk from", fp, "to", tp

def main():
    moveTower(3, 'A', 'B', 'C')

main()
