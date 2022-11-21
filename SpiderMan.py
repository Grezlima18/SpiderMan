import pygame
import random


pygame.init()
pygameDisplay = pygame.display
pygameDisplay.set_caption("Spider Man: The Game")
altura = 520
largura = 1000
tamanho = (largura, altura)
gameDisplay = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
gameEvents = pygame.event
branco = (255,255,255)
fundo = pygame.image.load("assets/fundo.jpg")
spider = pygame.image.load("assets/spider.png")
bomb = pygame.image.load("assets/bomb.png")




def escreverTexto (texto):
    fonte  = pygame.font.Font("freesansbold.ttf",15)
    textoDisplay = fonte.render(texto,True,branco)
    gameDisplay.blit(textoDisplay, (670,40))
    pygameDisplay.update()

def morreu():
    fonte  = pygame.font.Font("freesansbold.ttf",95)
    fonte2  = pygame.font.Font("freesansbold.ttf",45)
    textoDisplay = fonte.render("MORREUU !!!!",True,branco)
    textoDisplay2 = fonte2.render("press enter to continue !!!!",True,branco)
    gameDisplay.blit(textoDisplay, (150,150))
    gameDisplay.blit(textoDisplay2, (150,350))
    pygameDisplay.update()

def jogar():
    jogando = True
    spiderX = 500
    spiderY = 400
    movimentoSpiderX = 0
    larguraSpider = 120
    alturaSpider = 110
    alturaBomb = 256
    larguraBomb = 256
    posicaoBombX = 400
    posicaoBombY = -240
    velocidadeBomb = 1
    pontos = 0
    pygame.mixer.music.load("assets/spiderSong.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(-1)

    bombSound = pygame.mixer.Sound("assets/somBomb.mp3")
    bombSound.set_volume(1)
    pygame.mixer.Sound.play(bombSound)

    explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
    explosaoSound.set_volume(1)
    while True:
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimentoSpiderX = -15
                elif event.key == pygame.K_RIGHT:
                    movimentoSpiderX = 15
                elif event.key == pygame.K_RETURN:
                    jogar()
            elif event.type == pygame.KEYUP:
                movimentoSpiderX = 0
            
        if jogando:
            if posicaoBombY > altura:
                posicaoBombY = -240
                posicaoBombX = random.randint(0,largura)
                velocidadeBomb = velocidadeBomb + 1
                pontos = pontos + 1
                pygame.mixer.Sound.play(bombSound)
            else:
                posicaoBombY =posicaoBombY + velocidadeBomb

            if spiderX + movimentoSpiderX >0 and spiderX + movimentoSpiderX< largura-larguraSpider:
                spiderX = spiderX + movimentoSpiderX
            gameDisplay.fill(branco)
            gameDisplay.blit(fundo,(0,0))
            gameDisplay.blit(spider, (spiderX,spiderY))
            
            gameDisplay.blit(bomb, (posicaoBombX,posicaoBombY))
            escreverTexto("Pontos: "+str(pontos))

            pixelsXSpider = list(range(spiderX, spiderX+larguraSpider))
            pixelsYSpider = list(range(spiderY, spiderY+alturaSpider))

            pixelXBomb = list(range(posicaoBombX, posicaoBombX+larguraBomb))
            pixelYBomb = list(range(posicaoBombY, posicaoBombY+alturaBomb))

            colisaoY = len(list(set(pixelYBomb) & set(pixelsYSpider) ))
            if colisaoY > 0:
                colisaoX = len(list(set(pixelXBomb) & set(pixelsXSpider) ))
                if colisaoX > 45:
                    morreu()
                    jogando=False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(explosaoSound)


        pygameDisplay.update()
        clock.tick(60)

jogar()

