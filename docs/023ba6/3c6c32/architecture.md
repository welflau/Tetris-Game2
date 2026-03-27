# 架构设计 - 实现Game类 - 游戏主控制器

## 架构模式
MVC + 状态机模式

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生Canvas API
- **database**: LocalStorage（游戏状态持久化）
- **others**: ES6 Modules, Canvas 2D Context, RequestAnimationFrame

## 模块设计

### Game类（主控制器）
职责: 游戏状态管理、游戏循环控制、模块协调、事件分发
- init() - 游戏初始化
- start() - 开始游戏
- pause() - 暂停游戏
- reset() - 重置游戏
- update() - 游戏状态更新
- render() - 渲染协调
- handleInput(event) - 输入处理
- getGameState() - 获取游戏状态

### GameState状态管理
职责: 维护游戏状态枚举和状态转换逻辑
- setState(state) - 设置状态
- getState() - 获取当前状态
- canTransition(from, to) - 状态转换验证

### GameLoop游戏循环
职责: 管理游戏主循环、帧率控制、时间管理
- start() - 启动循环
- stop() - 停止循环
- setFPS(fps) - 设置帧率
- getDeltaTime() - 获取时间差

### EventManager事件管理
职责: 统一事件处理、键盘输入管理、事件分发
- bindEvents() - 绑定事件
- unbindEvents() - 解绑事件
- handleKeyDown(event) - 键盘按下
- handleKeyUp(event) - 键盘释放

### ScoreManager分数管理
职责: 分数计算、等级管理、统计数据
- addScore(points) - 添加分数
- getScore() - 获取分数
- getLevel() - 获取等级
- getLinesCleared() - 获取消除行数

## 数据流
用户输入 -> EventManager -> Game类 -> 状态验证 -> Board/Tetromino更新 -> ScoreManager计算 -> 渲染协调 -> Canvas输出。Game类作为中央调度器，接收输入事件，更新游戏状态，协调Board和Tetromino的交互，管理分数和等级，最终触发渲染更新。

## 风险点
- 游戏循环性能优化复杂度
- 状态管理复杂性随功能增加而提升
- 事件处理的内存泄漏风险
- 多模块协调的耦合度控制

## 关键决策
- 采用状态机模式管理游戏状态，确保状态转换的安全性
- 使用requestAnimationFrame实现游戏循环，保证流畅性
- Game类采用依赖注入方式管理Board和Tetromino实例
- 事件系统采用观察者模式，降低模块间耦合
- 游戏配置采用配置对象模式，便于调试和扩展
