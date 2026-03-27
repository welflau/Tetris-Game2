# 架构设计 - 实现Board类 - 游戏面板管理

## 架构模式
MVC模式 + 组件化架构

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: 原生Canvas API
- **database**: 内存存储（二维数组）
- **others**: HTML5 Canvas, ES6+ 模块系统, 事件驱动模式

## 模块设计

### Board核心类
职责: 管理10×20游戏网格状态，提供网格操作接口
- constructor(width=10, height=20) - 初始化面板
- getCell(x, y) - 获取指定位置网格状态
- setCell(x, y, value) - 设置指定位置网格状态
- isValidPosition(x, y) - 检查位置是否有效
- clearBoard() - 清空面板
- getBoard() - 获取完整面板状态

### 网格状态管理器
职责: 维护网格数据结构，处理网格状态变更
- initializeGrid() - 初始化网格数据
- updateGrid(x, y, state) - 更新网格状态
- validateBounds(x, y) - 边界检测
- getGridSnapshot() - 获取网格快照

### 碰撞检测器
职责: 处理方块与边界、其他方块的碰撞检测
- checkBoundaryCollision(x, y) - 边界碰撞检测
- checkBlockCollision(positions) - 方块碰撞检测
- isPositionOccupied(x, y) - 检查位置是否被占用

### 行消除管理器
职责: 检测和处理完整行的消除逻辑
- checkFullRows() - 检测完整行
- clearRow(rowIndex) - 清除指定行
- dropRowsAbove(rowIndex) - 上方行下落
- getCompletedRows() - 获取已完成行数

## 数据流
Board类使用二维数组存储网格状态(0=空，1-7=不同颜色方块)，通过网格状态管理器维护数据一致性，碰撞检测器提供位置验证，行消除管理器处理游戏逻辑，所有操作通过统一接口暴露给Game主控制器调用

## 风险点
- 网格坐标系统与Canvas渲染坐标可能不一致
- 二维数组索引越界风险
- 行消除时的数据同步问题
- 内存泄漏风险（频繁的数组操作）

## 关键决策
- 使用二维数组作为网格数据结构，平衡性能和可读性
- 采用0-based索引系统，与JavaScript数组保持一致
- 网格状态用数字表示，0为空，1-7为不同颜色方块
- 边界检测在Board层实现，提供统一的验证接口
- 行消除逻辑封装在独立模块，便于后续扩展计分系统
