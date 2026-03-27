# 架构设计 - 创建项目基础结构和HTML入口文件

## 架构模式
MVC + 模块化组件架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生JavaScript + HTML5 Canvas
- **database**: LocalStorage (本地存储)
- **others**: CSS3, HTML5, Canvas API, Web Audio API

## 模块设计

### HTML入口模块
职责: 提供游戏的基础页面结构，包含Canvas画布、UI控制面板、响应式布局
- Canvas元素接口
- UI控件事件绑定
- 响应式媒体查询

### CSS样式模块
职责: 定义游戏界面样式，实现响应式设计，提供视觉效果和动画
- 响应式断点
- CSS变量定义
- 动画关键帧

### 游戏引擎核心
职责: 管理游戏主循环，协调各个子模块，处理游戏状态转换
- init()
- start()
- pause()
- reset()
- update()
- render()

### 方块管理模块
职责: 定义7种方块类型，管理方块的生成、移动、旋转逻辑
- createTetromino()
- moveTetromino()
- rotateTetromino()
- getTetromino()

### 游戏板模块
职责: 管理游戏区域网格，处理方块放置、行消除、碰撞检测
- placeTetromino()
- clearLines()
- checkCollision()
- isGameOver()

### 输入控制模块
职责: 处理键盘和触摸输入，将用户操作转换为游戏指令
- bindKeyEvents()
- bindTouchEvents()
- handleInput()

### 渲染模块
职责: 负责Canvas绘制，包括游戏区域、方块、UI元素的渲染
- drawBoard()
- drawTetromino()
- drawUI()
- drawEffects()

### 计分系统模块
职责: 管理分数计算、等级提升、最高分记录
- updateScore()
- updateLevel()
- saveHighScore()
- getHighScore()

## 数据流
用户输入 -> 输入控制模块 -> 游戏引擎核心 -> 方块管理/游戏板模块 -> 计分系统 -> 渲染模块 -> Canvas显示。游戏引擎通过requestAnimationFrame驱动主循环，各模块通过事件系统和直接调用进行通信。

## 风险点
- Canvas在不同设备上的兼容性问题
- 响应式设计在移动端的触控体验
- 游戏性能在低端设备上的表现
- 浏览器兼容性问题

## 关键决策
- 采用原生JavaScript而非框架，确保轻量级和高性能
- 使用HTML5 Canvas进行游戏渲染，支持硬件加速
- 采用模块化设计，每个功能独立封装便于维护
- 使用CSS Grid和Flexbox实现响应式布局
- 通过LocalStorage实现本地数据持久化
- 使用requestAnimationFrame确保流畅的游戏循环
