# 架构设计 - 设计游戏基础架构和类结构

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生Canvas API
- **database**: LocalStorage (游戏状态持久化)
- **others**: HTML5 Canvas, CSS3, Web APIs

## 模块设计

### Game (游戏控制器)
职责: 游戏主循环控制、状态管理、事件协调
- init() - 游戏初始化
- start() - 开始游戏
- pause() - 暂停游戏
- reset() - 重置游戏
- update() - 游戏状态更新
- render() - 渲染调度

### Board (游戏面板)
职责: 网格状态管理、边界检测、行消除逻辑
- initGrid() - 初始化10x20网格
- isValidPosition(tetromino, x, y) - 位置有效性检测
- placeTetromino(tetromino) - 放置方块到网格
- clearLines() - 清除满行
- getGrid() - 获取网格状态
- render(context) - 渲染网格

### Tetromino (方块对象)
职责: 方块形状定义、旋转变换、位置管理
- constructor(type, x, y) - 创建指定类型方块
- rotate() - 顺时针旋转90度
- move(dx, dy) - 移动方块
- getShape() - 获取当前形状矩阵
- getPosition() - 获取当前位置
- clone() - 克隆方块对象

### Renderer (渲染器)
职责: Canvas渲染管理、坐标转换、视觉效果
- initCanvas() - Canvas初始化
- drawGrid() - 绘制网格线
- drawBlock(x, y, color) - 绘制单个方块
- drawTetromino(tetromino) - 绘制方块对象
- clear() - 清空画布

### InputHandler (输入处理器)
职责: 键盘事件处理、输入映射、防抖控制
- bindEvents() - 绑定键盘事件
- handleKeyDown(event) - 按键处理
- setKeyMap(keyMap) - 设置按键映射

### Utils (工具函数)
职责: 通用工具函数、常量定义、辅助方法
- TETROMINO_SHAPES - 方块形状常量
- COLORS - 颜色常量
- GRID_CONFIG - 网格配置
- deepClone(obj) - 深拷贝
- randomChoice(array) - 随机选择

## 数据流
用户输入 -> InputHandler -> Game控制器 -> Board状态更新 -> Tetromino对象操作 -> Renderer渲染输出。Game作为中央调度器，协调各模块间的数据流转，Board维护游戏状态，Tetromino封装方块逻辑，Renderer负责视觉呈现。

## 风险点
- Canvas性能优化需求
- 方块旋转边界检测复杂性
- 游戏循环帧率控制精度
- 不同浏览器兼容性问题

## 关键决策
- 采用MVC架构分离关注点，提高代码可维护性
- 使用原生Canvas API避免框架依赖，减少包体积
- 网格采用二维数组结构，便于状态管理和碰撞检测
- 方块形状用矩阵表示，支持灵活的旋转变换
- 渲染采用双缓冲机制，避免闪烁问题
- 输入处理独立模块化，支持自定义按键映射
