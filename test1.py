import pygame


def main():
    # 加载pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口的标题
    pygame.display.set_caption('大球吃小球')

    screen.fill((244, 244, 244))
    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    pygame.display.flip()
    # 加载背景图片
    ball_image = pygame.image.load('./images/1.jpg')
    # 在窗口上渲染图像
    screen.blit(ball_image,(50,50))
    # pygame.display.flip()

    x, y = 50, 50
    running = True
    while running:
        # 从消息队列中获取事件并对时间进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
