# 架构设计 - 投影方块配置优化

## 架构模式
分层架构（Layered Architecture）

## 技术栈

- **language**: JavaScript/TypeScript
- **framework**: HTML5 Canvas / WebGL
- **database**: LocalStorage（用户配置持久化）
- **others**: CSS3, Canvas 2D API, Web Storage API

## 模块设计

### GhostPieceRenderer
职责: 负责投影方块的渲染逻辑，包括透明度控制、轮廓绘制、颜色管理
- drawGhost(piece, position, style)
- setOpacity(value)
- setRenderMode(mode)

### GhostPieceConfig
职责: 管理投影方块的配置参数，包括透明度、渲染模式、颜色等设置
- getConfig()
- updateConfig(options)
- resetToDefault()
- validateConfig(config)

### UserPreferences
职责: 处理用户自定义设置的存储和读取，提供配置界面交互
- savePreferences(config)
- loadPreferences()
- exportSettings()
- importSettings(data)

### VisibilityTester
职责: 测试投影方块在不同背景和游戏状态下的可见性和对比度
- testVisibility(background, ghostStyle)
- calculateContrast()
- suggestOptimalSettings()

### GameRenderer
职责: 游戏主渲染器，协调各个渲染组件，确保视觉一致性
- render(gameState)
- updateGhostPiece()
- refreshDisplay()

## 数据流
用户通过设置界面调整投影方块参数 → UserPreferences保存配置到LocalStorage → GhostPieceConfig读取并验证配置 → GhostPieceRenderer根据配置渲染投影方块 → VisibilityTester实时检测可见性 → GameRenderer统一渲染到Canvas

## 风险点
- 不同设备和浏览器的Canvas渲染差异可能影响透明度效果
- 过度透明可能导致投影方块在某些背景下不可见
- 轮廓线模式在高分辨率屏幕上可能出现锯齿
- 用户自定义配置可能产生不合理的视觉效果

## 关键决策
- 采用Canvas 2D API而非WebGL以降低复杂度和兼容性问题
- 使用分层架构分离渲染逻辑和配置管理
- 提供多种预设模式（高透明、轮廓线、经典）供用户选择
- 实现实时预览功能让用户直观调整参数
- 使用LocalStorage持久化用户配置，避免依赖后端服务
