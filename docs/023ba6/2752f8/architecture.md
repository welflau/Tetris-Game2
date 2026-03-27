# 架构设计 - 实现Tetromino类 - 方块对象

## 架构模式
MVC + 组件化架构

## 技术栈

- **language**: JavaScript (ES6+)
- **framework**: 原生JavaScript + Canvas API
- **database**: 无（客户端游戏）
- **others**: HTML5 Canvas, CSS3, 模块化设计模式

## 模块设计

### Tetromino核心类
职责: 定义方块对象的基本属性、形状数据和状态管理
- constructor(type, x, y) - 初始化方块
- getShape() - 获取当前形状矩阵
- getPosition() - 获取当前位置
- getColor() - 获取方块颜色
- getType() - 获取方块类型

### 形状数据管理模块
职责: 存储和管理7种标准俄罗斯方块的形状定义
- TETROMINO_SHAPES - 形状数据常量
- TETROMINO_COLORS - 颜色映射常量
- getShapeMatrix(type, rotation) - 获取指定旋转状态的形状矩阵

### 方块操作模块
职责: 处理方块的基础操作方法
- move(dx, dy) - 移动方块
- setPosition(x, y) - 设置绝对位置
- clone() - 创建方块副本
- reset() - 重置方块状态

### 渲染接口模块
职责: 提供方块渲染所需的数据接口
- getRenderData() - 获取渲染数据
- getBoundingBox() - 获取边界框信息
- getActiveBlocks() - 获取活动方块坐标列表

## 数据流
Tetromino类接收类型和初始位置参数 -> 从形状数据管理模块获取对应的形状矩阵和颜色 -> 通过操作模块处理位置变更 -> 向渲染接口提供当前状态数据 -> Game类调用渲染接口获取数据进行Canvas绘制

## 风险点
- 形状数据结构设计不当可能影响后续旋转功能实现
- 坐标系统与Board类的网格系统不匹配
- 方块边界计算错误导致碰撞检测问题
- 内存管理不当导致方块对象创建过多

## 关键决策
- 采用4x4矩阵存储所有方块形状，统一数据结构便于处理
- 使用枚举常量定义7种标准方块类型（I、O、T、S、Z、J、L）
- 坐标系统采用左上角为原点，与Canvas坐标系保持一致
- 实现不可变对象设计，状态变更通过方法调用而非直接属性修改
- 预留旋转状态属性，为后续旋转功能实现做准备
