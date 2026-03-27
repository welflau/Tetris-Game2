# 架构设计 - 实现方块移动和旋转逻辑

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: HTML5 Canvas
- **database**: LocalStorage（游戏状态持久化）
- **others**: CSS3, Web APIs (requestAnimationFrame), Event Listeners

## 模块设计

### TetrominoController
职责: 管理当前活动方块的移动、旋转和下降逻辑
- moveLeft() - 向左移动方块
- moveRight() - 向右移动方块
- moveDown() - 向下移动方块
- rotate() - 顺时针旋转方块
- drop() - 硬降方块到底部
- getCurrentPosition() - 获取当前方块位置
- setPosition(x, y) - 设置方块位置

### RotationEngine
职责: 处理方块旋转算法和旋转状态管理
- rotateMatrix(matrix) - 矩阵旋转算法
- getRotationStates(type) - 获取方块所有旋转状态
- validateRotation(newState, position) - 验证旋转是否有效
- getWallKickData(type, rotation) - 获取墙踢数据

### MovementValidator
职责: 验证方块移动和旋转的合法性
- isValidPosition(tetromino, x, y) - 验证位置是否有效
- checkBoundaries(tetromino, x, y) - 检查边界碰撞
- checkCollision(tetromino, x, y) - 检查与已放置方块碰撞
- canMove(direction) - 检查是否可以移动
- canRotate() - 检查是否可以旋转

### InputHandler
职责: 处理键盘输入和按键响应
- bindKeyEvents() - 绑定键盘事件
- handleKeyDown(event) - 处理按键按下
- handleKeyUp(event) - 处理按键释放
- setKeyRepeat(key, callback) - 设置按键重复
- getInputState() - 获取当前输入状态

### AutoDropSystem
职责: 管理方块自动下降机制和时间控制
- startAutoDrop() - 开始自动下降
- stopAutoDrop() - 停止自动下降
- setDropSpeed(level) - 根据等级设置下降速度
- resetDropTimer() - 重置下降计时器
- forceDropTick() - 强制执行一次下降

### PositionCalculator
职责: 计算方块位置、偏移和坐标转换
- getAbsolutePosition(tetromino) - 获取方块绝对位置
- calculateOffset(direction) - 计算移动偏移量
- gridToPixel(x, y) - 网格坐标转像素坐标
- pixelToGrid(x, y) - 像素坐标转网格坐标
- getGhostPosition(tetromino) - 计算幽灵方块位置

## 数据流
InputHandler接收键盘输入 -> TetrominoController处理移动/旋转请求 -> MovementValidator验证操作合法性 -> RotationEngine处理旋转逻辑 -> PositionCalculator计算新位置 -> 更新游戏状态 -> 触发渲染更新。AutoDropSystem独立运行，定时触发下降操作。

## 风险点
- 旋转算法复杂度高，可能影响性能
- 按键响应延迟可能超过50ms要求
- 墙踢算法实现复杂，容易出现边界情况
- 自动下降与手动操作的时序冲突
- 不同浏览器的键盘事件兼容性问题

## 关键决策
- 采用标准SRS旋转系统确保游戏体验一致性
- 使用requestAnimationFrame确保60FPS流畅运行
- 实现按键防抖和重复机制提升操作手感
- 采用状态机模式管理方块的各种状态
- 使用事件驱动架构解耦输入处理和游戏逻辑
- 实现幽灵方块功能提升用户体验
