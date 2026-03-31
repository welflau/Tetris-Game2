# 架构设计 - 音效系统开发

## 架构模式
音效系统模块化架构

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生JavaScript + Web Audio API

## 模块设计

### AudioManager
职责: 音效资源管理，包括音频文件加载、缓存、音量控制
- loadAudio(audioName, audioPath)
- playSound(soundName, volume)
- setMasterVolume(volume)
- preloadAllSounds()

### SoundEffects
职责: 游戏音效播放控制，定义各种游戏事件对应的音效
- playMoveSound()
- playRotateSound()
- playDropSound()
- playLineClearSound(lines)
- playGameOverSound()
- playLevelUpSound()

### AudioSettings
职责: 音效设置管理，包括音量调节、静音控制、设置持久化
- toggleMute()
- setSoundVolume(volume)
- loadSettings()
- saveSettings()

## 数据流
游戏事件触发 -> SoundEffects接收事件 -> AudioManager播放对应音效 -> Web Audio API输出声音，同时AudioSettings管理用户音效偏好设置并通过LocalStorage持久化

## 关键决策
- 使用Web Audio API而非HTML5 Audio元素，提供更好的性能和控制能力
- 采用音效预加载策略，避免游戏过程中的延迟
- 实现音效分层管理（背景音乐、音效、UI音效）
- 集成到现有游戏引擎事件系统，通过事件监听触发音效
- 使用LocalStorage保存用户音效设置偏好
- 支持音效文件格式：MP3、OGG、WAV，确保浏览器兼容性
