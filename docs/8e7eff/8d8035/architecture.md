# 架构设计 - 功能模块划分和接口设计

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas + Web Audio API
- **database**: LocalStorage/IndexedDB
- **others**: Webpack, ESLint, Jest, CSS3

## 模块设计

### GameEngine
职责: 游戏核心引擎，管理游戏循环、状态机和全局事件
- start(): void - 启动游戏
- pause(): void - 暂停游戏
- reset(): void - 重置游戏
- update(deltaTime: number): void - 更新游戏状态
- render(): void - 渲染游戏画面

### GameBoard
职责: 管理游戏面板，处理方块放置、行消除和碰撞检测
- placeTetromino(tetromino: Tetromino): boolean - 放置方块
- clearLines(): number[] - 清除满行
- checkCollision(tetromino: Tetromino, x: number, y: number): boolean - 碰撞检测
- getBoard(): number[][] - 获取面板状态
- reset(): void - 重置面板

### TetrominoManager
职责: 管理俄罗斯方块的生成、旋转、移动和形状定义
- generateNext(): Tetromino - 生成下一个方块
- getCurrentTetromino(): Tetromino - 获取当前方块
- rotateTetromino(direction: string): boolean - 旋转方块
- moveTetromino(dx: number, dy: number): boolean - 移动方块
- getPreview(): Tetromino[] - 获取预览方块队列

### InputController
职责: 处理用户输入，包括键盘、触摸和鼠标事件
- bindEvents(): void - 绑定输入事件
- unbindEvents(): void - 解绑输入事件
- onKeyDown(callback: Function): void - 键盘按下事件
- onKeyUp(callback: Function): void - 键盘释放事件
- setKeyMapping(mapping: object): void - 设置按键映射

### ScoreManager
职责: 管理游戏分数、等级、统计数据和排行榜
- addScore(lines: number): void - 添加分数
- getScore(): number - 获取当前分数
- getLevel(): number - 获取当前等级
- getStatistics(): object - 获取游戏统计
- saveHighScore(): void - 保存最高分
- getHighScores(): number[] - 获取排行榜

### Renderer
职责: 负责游戏画面渲染，包括方块、背景、特效和UI元素
- renderBoard(board: number[][]): void - 渲染游戏面板
- renderTetromino(tetromino: Tetromino): void - 渲染当前方块
- renderPreview(tetrominos: Tetromino[]): void - 渲染预览区
- renderUI(gameState: object): void - 渲染UI界面
- renderEffects(): void - 渲染特效动画

### AudioManager
职责: 管理游戏音效和背景音乐的播放
- playSound(soundName: string): void - 播放音效
- playMusic(musicName: string): void - 播放背景音乐
- stopMusic(): void - 停止背景音乐
- setVolume(volume: number): void - 设置音量
- mute(isMuted: boolean): void - 静音控制

### ConfigManager
职责: 管理游戏配置、设置和本地存储
- loadConfig(): object - 加载配置
- saveConfig(config: object): void - 保存配置
- getSetting(key: string): any - 获取设置项
- setSetting(key: string, value: any): void - 设置配置项
- resetToDefault(): void - 重置为默认配置

### UIManager
职责: 管理游戏界面，包括菜单、对话框和HUD显示
- showMenu(menuType: string): void - 显示菜单
- hideMenu(): void - 隐藏菜单
- showDialog(dialogType: string, data: object): void - 显示对话框
- updateHUD(gameState: object): void - 更新HUD显示
- bindUIEvents(): void - 绑定UI事件

### EffectManager
职责: 管理游戏特效，包括消行动画、粒子效果等
- playLineClearEffect(lines: number[]): void - 播放消行特效
- playLevelUpEffect(): void - 播放升级特效
- playTetrisEffect(): void - 播放四行消除特效
- updateEffects(deltaTime: number): void - 更新特效状态
- clearAllEffects(): void - 清除所有特效

## 数据流
GameEngine作为中央控制器，协调各模块间的数据流。InputController接收用户输入并通知GameEngine，GameEngine更新TetrominoManager和GameBoard状态，ScoreManager计算分数和等级，Renderer根据游戏状态渲染画面，AudioManager播放相应音效，UIManager更新界面显示，ConfigManager负责数据持久化。所有模块通过事件系统进行松耦合通信。

## 风险点
- 模块间接口设计不当可能导致紧耦合
- 事件系统复杂度过高影响性能
- Canvas渲染性能在低端设备上可能不足
- 音频兼容性问题在不同浏览器间存在差异
- 本地存储容量限制影响数据保存

## 关键决策
- 采用MVC+组件化架构确保代码可维护性
- 使用事件驱动模式实现模块间解耦
- 选择Canvas 2D API平衡性能和兼容性
- 使用TypeScript提高代码质量和开发效率
- 采用模块化设计支持功能扩展和测试
- 使用LocalStorage作为主要存储方案，IndexedDB作为备选
