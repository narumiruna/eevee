# Hardfork Analysis

## [Release notes from heimdall](https://github.com/maticnetwork/heimdall/releases.atom)

### v1.1.0-beta (2024-11-27 07:28:44)
```

This release primarily contains :

* Changes proposed in [PIP-52](https://forum.polygon.technology/t/pip-52-execution-derived-randomness-for-producer-selection/20193) which will be activated by the `Jorvik` **hardfork** on **amoy testnet**.
* Enabling of GRPC communication between heimdall and bor.
* Optimizations for exporting app module state.
* Bug fixes as usual.

What's Changed
--------------

* Docs fix spelling issues by [@nnsW3](https://github.com/nnsW3) in [#1194](https://github.com/m...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.1.0-beta
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本與硬分叉有關，因為它包含將在 amoy 測試網上啟用的 PIP-52 中提出的變更，並提到 Jorvik 硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names: amoy
- 📅 Upgrade Deadline: None

### v1.0.10 (2024-10-09 15:02:56)
```

What's Changed
--------------

* Fix typos by [@omahs](https://github.com/omahs) in [#1182](https://github.com/maticnetwork/heimdall/pull/1182)
* Refactored packager tooling, cleanup, shasums, etc. by [@djpolygon](https://github.com/djpolygon) in [#1185](https://github.com/maticnetwork/heimdall/pull/1185)
* Adding rpm packagers by [@djpolygon](https://github.com/djpolygon) in [#1187](https://github.com/maticnetwork/heimdall/pull/1187)
* Backport master to develop by [@marcello33](https://githu...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.10
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤和改進工具，並未顯示出任何重大變更或破壞性改動，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.9 (2024-10-09 14:58:13)
```

This release contains some improvements and bug fixes.

What's Changed
--------------

* Backport master to develop by [@marcello33](https://github.com/marcello33) in [#1168](https://github.com/maticnetwork/heimdall/pull/1168)
* Handle account sequence correctly in bridge by [@Raneet10](https://github.com/Raneet10) in [#1170](https://github.com/maticnetwork/heimdall/pull/1170)
* server: add status endpoint from tendermint by [@manav2401](https://github.com/manav2401) in [#1175](https://github....```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.9
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含一些改進和錯誤修正，並未涉及協議的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.9-beta (2024-10-02 09:50:23)
```

What's Changed
--------------

* Backport master to develop by [@marcello33](https://github.com/marcello33) in [#1168](https://github.com/maticnetwork/heimdall/pull/1168)
* Handle account sequence correctly in bridge by [@Raneet10](https://github.com/Raneet10) in [#1170](https://github.com/maticnetwork/heimdall/pull/1170)
* server: add status endpoint from tendermint by [@manav2401](https://github.com/manav2401) in [#1175](https://github.com/maticnetwork/heimdall/pull/1175)
* build(deps): bump...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.9-beta
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤和增強功能，並未顯示出任何需要進行硬分叉的重大變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.8-beta (2024-07-16 07:23:39)
```

This is a maintenance release for heimdall which adds a new `/status` endpoint to heimdall's rest-server.

What's Changed
--------------

* server: add status endpoint from tendermint by [@manav2401](https://github.com/manav2401) in [#1175](https://github.com/maticnetwork/heimdall/pull/1175)

**Full Changelog**: [v1.0.7...v1.0.8-beta](https://github.com/maticnetwork/heimdall/compare/v1.0.7...v1.0.8-beta)

```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.8-beta
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為維護更新，僅新增了一個 /status 端點，並未引入任何破壞性變更或重大新功能，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.7 (2024-06-05 14:36:41)
```

This release contains minor improvements and bug fixes.

What's Changed
--------------

* chore: enforce capitalisation in flags description by [@leovct](https://github.com/leovct) in [#1137](https://github.com/maticnetwork/heimdall/pull/1137)
* Fix path for `matic-cli` dockerized tests by [@marcello33](https://github.com/marcello33) in [#1139](https://github.com/maticnetwork/heimdall/pull/1139)
* POS-2399: ganache bug workaround to reduce `smoke_test` time in CI by [@marcello33](https://githu...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.7
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新僅包含小幅改進和錯誤修復，並未提及任何重大變更或強制升級的要求，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.7-beta (2024-06-04 06:10:11)
```

This release contains minor improvements and bug fixes.

What's Changed
--------------

* chore: enforce capitalisation in flags description by [@leovct](https://github.com/leovct) in [#1137](https://github.com/maticnetwork/heimdall/pull/1137)
* Fix path for `matic-cli` dockerized tests by [@marcello33](https://github.com/marcello33) in [#1139](https://github.com/maticnetwork/heimdall/pull/1139)
* POS-2399: ganache bug workaround to reduce `smoke_test` time in CI by [@marcello33](https://githu...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.7-beta
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含小幅改進和錯誤修復，並未顯示出任何需要進行硬分叉的重大變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.6 (2024-05-23 15:20:51)
```

This release contains a fix for the milestone/checkpoint module

What's Changed
--------------

* Fix bb-31177 by [@marcello33](https://github.com/marcello33) in [#1163](https://github.com/maticnetwork/heimdall/pull/1163)

**Full Changelog**: [v1.0.5...v1.0.6](https://github.com/maticnetwork/heimdall/compare/v1.0.5...v1.0.6)

```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.6
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本僅包含對里程碑/檢查點模塊的修復，並未提及任何重大變更或不向後兼容的更新，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.6-beta-1 (2024-05-06 11:14:48)
```

**Full Changelog**: [v1.0.5...v1.0.6-beta-1](https://github.com/maticnetwork/heimdall/compare/v1.0.5...v1.0.6-beta-1)

```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.6-beta-1
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本的釋出包含了從先前版本的重大變更，並且可能需要所有節點進行升級以確保網絡的正常運行，因此這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.0.5 (2024-03-26 06:16:24)
```

This release contains a bug fix.

What's Changed
--------------

* Bump google.golang.org/protobuf from 1.31.0 to 1.33.0 by [@dependabot](https://github.com/dependabot) in [#1147](https://github.com/maticnetwork/heimdall/pull/1147)
* bridge, staking: chg: bug fix by [@marcello33](https://github.com/marcello33) in [#1149](https://github.com/maticnetwork/heimdall/pull/1149)
* Bump version to v1.0.5 by [@cffls](https://github.com/cffls) in [#1150](https://github.com/maticnetwork/heimdall/pull/115...```

- 🔗 Link: https://github.com/maticnetwork/heimdall/releases/tag/v1.0.5
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含錯誤修正和依賴更新，這些通常不需要硬分叉。沒有顯著的協議或共識規則變更，因此這不是硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from bor](https://github.com/maticnetwork/bor/releases.atom)

### v1.5.3-beta (2024-12-10 08:05:42)
```

What's Changed
--------------

* chore: fix function name by [@luozexuan](https://github.com/luozexuan) in [#1349](https://github.com/maticnetwork/bor/pull/1349)
* Backport master to develop (v1.5.2) by [@pratikspatil024](https://github.com/pratikspatil024) in [#1369](https://github.com/maticnetwork/bor/pull/1369)
* Limit bytes during response body read by [@marcello33](https://github.com/marcello33) in [#1370](https://github.com/maticnetwork/bor/pull/1370)
* Implement gRPC bidirectional commu...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.3-beta
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.5.3-beta 的更新內容主要是修復錯誤和增強功能，並未顯示出任何重大變更或強制升級的要求，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.2 (2024-10-30 15:55:36)
```

What's Changed
--------------

* Fix getBlockTransactionCountByNumber/Hash by [@cffls](https://github.com/cffls) in [#1365](https://github.com/maticnetwork/bor/pull/1365)
* Bump version to v1.5.2 by [@cffls](https://github.com/cffls) in [#1366](https://github.com/maticnetwork/bor/pull/1366)

**Full Changelog**: [v1.5.1...v1.5.2](https://github.com/maticnetwork/bor/compare/v1.5.1...v1.5.2)

```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本更新僅包含錯誤修正和版本提升，並未引入重大變更或共識機制的調整，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.1 (2024-10-30 14:50:56)
```

What's Changed
--------------

* Fix bor logs missing by [@cffls](https://github.com/cffls) in [#1361](https://github.com/maticnetwork/bor/pull/1361)
* Fix panic on nil block in ethstats by [@cffls](https://github.com/cffls) in [#1360](https://github.com/maticnetwork/bor/pull/1360)
* Bump version to v1.5.1 by [@cffls](https://github.com/cffls) in [#1362](https://github.com/maticnetwork/bor/pull/1362)

**Full Changelog**: [v1.5.0...v1.5.1](https://github.com/maticnetwork/bor/compare/v1.5.0...v1...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤，並未引入重大變更或共識規則的改動，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0 (2024-10-28 15:27:52)
```

What's Changed
--------------

* Add test for concurrent revert in MVHashmap by [@cffls](https://github.com/cffls) in [#1326](https://github.com/maticnetwork/bor/pull/1326)
* Log info about mismatched valset by [@cffls](https://github.com/cffls) in [#1325](https://github.com/maticnetwork/bor/pull/1325)
* Upstream merge 1.14.6 by [@anshalshukla](https://github.com/anshalshukla) in [#1300](https://github.com/maticnetwork/bor/pull/1300)
* Backporting master to develop by [@cffls](https://github.c...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本更新包含多項修正和改進，但沒有顯示出任何會導致硬分叉的重大變更或強制升級的要求。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta6 (2024-10-23 02:30:11)
```No content.```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta6
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.5.0-beta6 沒有顯示出硬分叉的跡象，因為它是測試版，且沒有重大更新或強制升級的要求。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta5 (2024-10-17 04:02:07)
```

What's Changed
--------------

* Changing names of pbss profiles for consistency in deb and rpm by [@djpolygon](https://github.com/djpolygon) in [#1356](https://github.com/maticnetwork/bor/pull/1356)

**Full Changelog**: [v1.5.0-beta4...v1.5.0-beta5](https://github.com/maticnetwork/bor/compare/v1.5.0-beta4...v1.5.0-beta5)

```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta5
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新僅涉及命名一致性，並未引入重大變更或破壞性改動，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta4 (2024-10-15 18:49:12)
```

What's Changed
--------------

* Adding refactored packager, adding pbss configs, removal of mumbai ( … by [@djpolygon](https://github.com/djpolygon) in [#1311](https://github.com/maticnetwork/bor/pull/1311)
* Adding rpm packagers by [@djpolygon](https://github.com/djpolygon) in [#1339](https://github.com/maticnetwork/bor/pull/1339)
* Check block number and timestamp options when filtering conditional transactions by [@jj1980a](https://github.com/jj1980a) in [#1350](https://github.com/maticnet...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta4
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是增強功能和配置，並未涉及共識機制或交易驗證規則的重大變更，因此不需要進行硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta3 (2024-10-09 16:49:05)
```

What's Changed
--------------

* internal/cli: add prometheus sever timeouts by [@marcello33](https://github.com/marcello33) in [#1344](https://github.com/maticnetwork/bor/pull/1344)
* [Fix panic on getting safe block](https://github.com/maticnetwork/bor/commit/a7578a3ceab74b0551b115dd1a3250d7e870a329)
* [Fix tx index limit not being used correctly](https://github.com/maticnetwork/bor/commit/48bdfa7ffbfb8da50fbc3bbef54882d3b80e698f)
* [Fix bor tx missing](https://github.com/maticnetwork/bor/co...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta3
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤和性能改進，並未提及任何重大變更或需要強制升級的內容，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta2 (2024-10-04 17:59:14)
```

What's Changed
--------------

* Fix panic in eth\_getLogs by [@cffls](https://github.com/cffls) in [#1342](https://github.com/maticnetwork/bor/pull/1342)

**Full Changelog**: [v1.5.0-beta...v1.5.0-beta2](https://github.com/maticnetwork/bor/compare/v1.5.0-beta...v1.5.0-beta2)

```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新僅包含錯誤修正，並未引入重大變更或破壞性改動，因此不需要進行硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-beta (2024-10-03 17:49:48)
```

The major change in this release is the commits merged from [go-ethereum](https://github.com/ethereum/go-ethereum/)  up to geth 1.14.6.

What's Changed
--------------

* Add test for concurrent revert in MVHashmap by [@cffls](https://github.com/cffls) in [#1326](https://github.com/maticnetwork/bor/pull/1326)
* Log info about mismatched valset by [@cffls](https://github.com/cffls) in [#1325](https://github.com/maticnetwork/bor/pull/1325)
* Upstream merge 1.14.6 by [@anshalshukla](https://github...```

- 🔗 Link: https://github.com/maticnetwork/bor/releases/tag/v1.5.0-beta
- 🟢 Hardfork: no
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本不顯示出硬分叉的跡象，因為它主要是從 go-ethereum 合併的更新，並且沒有明確的破壞性變更或強制升級的通知。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from go-ethereum](https://github.com/ethereum/go-ethereum/releases.atom)

### Gei Hinnom (v1.14.12) (2024-11-19 13:53:28)
```

This release covers quite a lot of time, and has many changes across the codebase. In particular; changes in tracing and account management, optimizations in database, trie and evm, and, as always bugfixes.

This release removes the `personal` RPC namespace. It was already previously deprecated, and has not been accessible by default for nearly two years. We also removed the `--unlock` command-line parameter, with a view towards removing key/account management from the `geth` binary.

* Key ma...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.12
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本的更新包含了多項重大變更，包括移除 `personal` RPC 名稱空間和 `--unlock` 命令行參數，這些都表明了功能上的重大改變。此外，針對追蹤和數據庫的優化也可能導致與舊版本的不兼容。這些因素共同表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Makhaira (v1.14.11) (2024-10-01 13:25:38)
```

This is a minor release, with the primary goal of publishing new `stable` and `latest` docker images. A problem in the CI pipeline prevented the publishing of docker images. We have now resolved the problem, and hope that the `v1.14.11`-release will be published as usual on Docker hub.

We have now switched the way the docker images are built, and the `-amd64` and `-arm64`-tagged versions **will no longer be maintained**:

* `alltools-latest-amd64`, `alltools-latest-arm64` -> **`alltools-lates...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.11
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為小型更新，主要目的是發布新的 Docker 映像，並解決 CI 管道中的問題。更新內容不涉及協議的重大變更，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Kopis (v1.14.10) (2024-09-27 11:15:39)
```

Geth v1.14.10 is a hotfix release to fix a [blob pool regression](https://github.com/ethereum/go-ethereum/pull/30518) introduced in v1.14.9. Users running the previous bad version should update ASAP. That said, there is no immediate danger to these users, just to the health of blob transaction propagation and inclusion in the network.

Beside the hotfix, this release:

* Ships stateless witness production and verification into the engine API ([#30069](https://github.com/ethereum/go-ethereum/pu...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.10
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: Geth v1.14.10 是一個熱修復版本，主要用於修復 v1.14.9 中引入的回歸問題。雖然建議用戶儘快更新，但這並不構成硬分叉，因為它不改變共識規則。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Aegis (v1.14.9) (2024-09-27 09:14:58)
```

***This release has been nuked. It broke the blob pool, please do not use it.***

---

This is a maintenance release, but also introduces support for the new multicall spec, which is a much anticipated feature providing a `eth_simulateV1` call, that takes a list of blocks and executes them as if calling multiple `eth_call`s sequentially. It accepts optional state and precompile overrides, as well as transfer log events. This release also ships with improved verkle support.

Command line
------...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.9
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本被標記為「已銷毀」，因為它破壞了 blob pool，並且不應使用。儘管引入了一些新功能，但由於存在關鍵錯誤，這個版本不應被視為有效的升級或硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Rayingri (v1.14.8) (2024-08-14 08:26:26)
```

This is a maintenance release with bug fixes only.

### Command changes

* Blobpool related flags in Geth now actually work. ([#30203](https://github.com/ethereum/go-ethereum/pull/30203))
* The `evm run` command no longer overwrites the sender account in genesis.json. ([#30259](https://github.com/ethereum/go-ethereum/pull/30259))
* `evm run` now allows configuring `baseFeePerGas` in genesis.json. ([#30281](https://github.com/ethereum/go-ethereum/pull/30281))

### Go API

* `core/types.Transact...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.8
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為維護版本，僅包含錯誤修正，並未引入任何共識規則或網絡協議的變更，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Trident (v1.14.7) (2024-07-11 12:37:41)
```

This is a hot-fix release for a bug ([#30139](https://github.com/ethereum/go-ethereum/issues/30139)) which affects only the previous release. Users of v1.14.6 are kindly requested to update.

For a full rundown of the changes please consult the Geth [1.14.7 release milestone](https://github.com/ethereum/go-ethereum/milestone/170?closed=1).

---

As with all our previous releases, you can find the:

* Pre-built binaries for all platforms on our [downloads page](https://geth.ethereum.org/downloa...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.7
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是針對前一版本（v1.14.6）的一個熱修復，並未引入重大變更或新功能，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Talaria (v1.14.6) (2024-07-03 07:55:42)
```

Geth v1.14.6 is a maintenance release, but it does ship with the *experimental* witness building validation code used in [@karalabe](https://github.com/karalabe)'s ["cross validation" proposal](https://gist.github.com/karalabe/47c906f0ab4fdc5b8b791b74f084e5f9). Note that the engine API part is not included in this release.

---

Shipped features:

* Add stateless witness builder and (self-)cross validator ([#29719](https://github.com/ethereum/go-ethereum/pull/29719), [#29807](https://github.co...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.6
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本為維護版本，並未引入任何需要全網升級的共識變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Bothros (v1.14.5) (2024-06-06 14:13:33)
```

Geth v1.14.5 is a hotfix release that addresses a regression introduced in v1.14.4, which prevented the node from discovering other peers in certain networking setups ([#29944](https://github.com/ethereum/go-ethereum/pull/29944)). It is otherwise identical to [v1.14.4](https://github.com/ethereum/go-ethereum/releases/tag/v1.14.4).

---

Geth v1.14.4 in a usual maintenance release, but it does ship a 5-7% block import [speed improvement](https://github.com/ethereum/go-ethereum/pull/29519). Furt...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.5
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.14.5 是一個熱修復版本，主要修復了 v1.14.4 中引入的回歸問題，並未引入任何新的功能或改變，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Triodia (v1.14.4) (2024-06-05 08:12:17)
```

Geth v1.14.4 in a usual maintenance release, but it does ship a 5-7% block import [speed improvement](https://github.com/ethereum/go-ethereum/pull/29519). Furthermore, v1.14.4 also finally includes an [Ether supply live tracer](https://github.com/ethereum/go-ethereum/pull/29347), that you can enable via `--vmtrace supply`. Also please note, the default value for miner tip enforcement was dropped from 1 gwei to 0.001 gwei (block producers can change this via `--miner.gasprice`).

Shipped featur...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.4
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是維護性質，包含性能改進和錯誤修正，並未引入任何共識規則的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Fuel Depot (v1.14.3) (2024-05-09 12:49:36)
```

We're issuing this (v1.14.3) release to finally publish v1.14 on the Ubuntu PPA. It is otherwise identical to [v1.14.2](https://github.com/ethereum/go-ethereum/releases/tag/v1.14.2).

---

This is a maintenance release containing bug-fixes. In case you are wondering where v1.14.1 (and v1.14.2) went, let's just say, the continuous integration gods have not been good to us.

List of changes in detail:

#### Geth

* When using `geth --dev` with a custom genesis block, the genesis file must now se...```

- 🔗 Link: https://github.com/ethereum/go-ethereum/releases/tag/v1.14.3
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.14.3 是一個維護更新，主要包含錯誤修復，並未引入任何需要硬分叉的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from omnicore](https://github.com/OmniLayer/omnicore/releases.atom)

### Omni Core v0.12.0 (2023-04-11 15:13:01)
```

v0.12.0 is a major release and adds the ability to send tokens from one address to multiple receivers within one transaction.

This release is mandatory and changes the rules of the Omni Layer protocol. An upgrade is required.

Upgrading from Omni Core 0.11 does not require a rescan and can be done very fast with minimal interruption.

Please report bugs using the issue tracker on GitHub:

<https://github.com/OmniLayer/omnicore/issues>

Table of contents
=================

* Omni Core v0.12.0
...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.12.0.1
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本是強制升級，並且改變了Omni Layer協議的規則，這表明它是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.12.0 (2023-02-14 14:57:47)
```

Omni Core 0.12.0

```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.12.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的釋出說明中沒有提及任何重大變更或強制升級的要求，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.11.0 (2021-09-07 14:57:55)
```

v0.11.0 is a major release and adds the ability to issue non-fungible token and to delegate the management of a token.

The delegation of token management will go live with block 702250, which is expected to be on or about 26rd September, 2021.

This release is mandatory and after the activation of the new features, the rules of the Omni Layer protocol are changed and incompatible with older versions of Omni Core. An upgrade is required.

A note will be shown within Omni Core and on the [Omni ...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.11.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本的發布引入了非同質化代幣的發行能力和代幣管理的委託功能，這些變更將使舊版本不再兼容，因此必須升級。
- 🔢 Block Number: 702250
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2021-09-26T00:00:00Z

### Omni Core v0.10.0 (2021-04-12 10:07:31)
```

v0.10.0 is a major release and updates the underlying version of Bitcoin Core from 0.18.1 to 0.20.1. This comes with a significant number of changes. In this version recovering from a hard shutdown or crash was also greatly improved.

While this release is not mandatory and doesn't change the consensus rules of the Omni Layer protocol, an upgrade is nevertheless recommended.

**Due to the upgrade from Bitcoin Core 0.18.1 to 0.20.1, this version incooperates many changes, so please take your ti...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.10.0
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本的更新不改變Omni Layer協議的共識規則，因此不算作硬分叉。儘管如此，升級仍然被建議以獲得更好的性能和功能。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.9.0 (2021-07-15 15:26:47)
```

v0.9.0 is a major release and uses Segregated Witness wrapped in P2SH for newly generated addresses per default. It also adds two new transaction types to anchor arbitrary data in the blockchain. As an experimental feature, several new commands were added to support querying any Bitcoin balance.

While this release is not mandatory and doesn't change the consensus rules of the Omni Layer protocol, an upgrade is nevertheless recommended.

Upgrading from 0.8.2, 0.8.1 or 0.8.0 does not require a ...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.9.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新不改變Omni Layer協議的共識規則，並且升級不是強制性的，因此這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.8.2 (2020-05-08 10:04:27)
```

v0.8.2 is a minor release and adds new RPCs to interact with the distributed exchange, which can be used to trade any tokens for bitcoins. It also incorporates significant performance improvements for the initial synchronization and upgrading from older versions of Omni Core.

Upgrading from 0.8.1 does not require a rescan and can be done very fast without interruption.

Please report bugs using the issue tracker on GitHub:

<https://github.com/OmniLayer/omnicore/issues>

Table of contents
===...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.8.2
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: Omni Core v0.8.2 是一個小版本更新，增加了新的 RPC 和性能改進，並且從 0.8.1 升級不需要重新掃描，這表明底層區塊鏈數據結構沒有重大變化，因此這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.8.1 (2020-03-25 09:40:43)
```

v0.8.1 is a minor release and includes significant performance improvements for the initial synchronization and upgrading from older versions of Omni Core.

A consensus affecting issue in an earlier version of Omni Core has been identified, which may cause some transactions to be executed twice. This has been addressed and fixed in the previous major version 0.8.0.

The first time you start this version from a version older than 0.8.0, the internal database for Omni Layer transactions is recon...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.8.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: Omni Core v0.8.1 是一個小版本更新，主要包括性能改進和修復先前版本中的問題。該版本沒有引入破壞性變更，也未提及必須升級的要求，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.8.0 (2020-03-03 10:52:56)
```

v0.8.0 is a major release and an upgrade is required.

A consensus affecting issue in an earlier version of Omni Core has been identified, which may cause some transactions to be executed twice. This has been addressed and fixed in this release.

More information about this issue will be announced on <https://blog.omni.foundation/>.

The first time you start this version, the internal database for Omni Layer transactions is reconstructed, which may consume several hours or even more than a day...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.8.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: Omni Core v0.8.0 是一個重大版本，並且需要升級。這次升級修復了早期版本中的共識影響問題，並且首次啟動時需要重建內部數據庫，這表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.7.1 (2020-01-22 06:26:00)
```

Omni Core 0.7.1 paves the way for trading any asset on the Omni Layer for Bitcoin in a decentralized fashion. It adds new commands to accept and execute orders on the distributed exchange.

Please note, if you have not yet upgraded from 0.6 or earlier versions: Omni Core 0.7 changed the code base of Omni Core from Bitcoin Core 0.13.2 to Bitcoin Core 0.18.1. Once consensus affecting features are enabled, this version is no longer compatible with previous versions and an upgrade is required. Due...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.7.1
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: Omni Core v0.7.1 版本的發布包含了從 Bitcoin Core 0.13.2 到 0.18.1 的重大變更，這導致了與舊版本的不兼容性，並且需要進行升級以繼續使用。這些變更包括數據庫重建和共識影響功能的啟用，這些都表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Omni Core v0.7.0 (2019-11-07 12:52:20)
```

v0.7.0 is a major release and changes the code base of Omni Core from Bitcoin Core 0.13.2 to Bitcoin Core 0.18.1. Once consensus affecting features are enabled, this version is no longer compatible with previous versions and an upgrade is required.

Compared to Omni Core v0.6.0 and previous versions, v0.7.0 enhances it's distributed exchange and supports trading of any asset or token for Bitcoin. This version also fixes locking issues and the RPCs for funding transactions as well as omni\_list...```

- 🔗 Link: https://github.com/OmniLayer/omnicore/releases/tag/v0.7.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本是一次重大更新，將Omni Core的代碼基礎從Bitcoin Core 0.13.2升級到0.18.1，並且一旦啟用共識影響的功能，該版本將不再與以前的版本兼容，因此需要進行升級。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from prysm](https://github.com/prysmaticlabs/prysm/releases.atom)

### v5.2.0-rc.2: `searchForPeers`: Replace `batchSize` by `batchPeriod`. (#14704) (2024-12-10 04:52:02)
```

Rationale:

Before this commit, the internal loop exited if:

* the expected amount of peers is found, or,
* the iterator returns `false` (exhaustion), or
* `batchSize` iterations are done.

The issue with the iterations count is, in case not enough

peer are found AND `iterator.Next` always returns `true`,

we don't control WHEN the loop is going to stop.

The root cause is we don't control the time needed to

run the `iterator.Next` function, which is a function of

`devp2P (geth)`...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.2.0-rc.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是針對內部性能的優化，並未改變協議的基本規則或數據結構，因此不需要進行硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.2.0-rc.1 (2024-12-10 01:37:19)
```

Revert "Proposer checks gas limit before accepting builder's bid" ([#1](https://github.com/prysmaticlabs/prysm/pull/1)…

```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.2.0-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新僅是撤回先前的更改，並未引入重大變更或不相容的更新，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.2.0-rc.0: Check kzg commitment for beacon-api propose block (#14702) (2024-12-09 14:38:28)
```

Co-authored-by: Preston Van Loon [pvanloon@offchainlabs.com](mailto:pvanloon@offchainlabs.com)

```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.2.0-rc.0
- 🟡 Hardfork: unknown
- 📊 Confidence: 60.0%
- 📝 Explanation: 此版本的釋出說明中並未明確提到必須升級，但由於其包含的變更可能會影響網絡的運作，因此存在潛在的硬分叉風險。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Mekong testnet release (v5.1.2) (2024-11-07 18:39:34)
```

v5.1.2-mekong
=============

This release is based on v5.1.2 with support for the `--mekong` testnet flag.

See the [full diff of changes since v5.1.2](https://github.com/prysmaticlabs/prysm/compare/v5.1.2...v5.1.2-mekong).

Here are some examples for how to run this pre-release. Note that some flags are not present, see the "How to run Mekong" link below for more accurate instructions.

```
# Using prysm.sh
USE_PRYSM_VERSION=v5.1.2-mekong ./prysm.sh beacon-chain --mekong

# Using docker
doc...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.1.2-mekong
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是基於 v5.1.2 的增量更新，主要是為了支持新的測試網路標誌，並不會對主網造成影響，因此不算作硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names: mekong
- 📅 Upgrade Deadline: None

### v5.1.3-rc.0 (2024-11-06 17:48:17)
```

[v5.1.3-rc.0](https://github.com/prysmaticlabs/prysm/compare/v5.1.2...v5.1.3-rc.0)
----------------------------------------------------------------------------------

This is a release candidate for v5.1.3. It has some important bug fix issues from v5.1.1 and v5.1.2 releases.

We want to test the release a bit more to ensure we have fixed any further known issues and we welcome users to test this release candidate, if they desire.

**Test via prysm.sh**

```
# Set environment variable `USE_P...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.1.3-rc.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是針對 v5.1.3 的候選版本，並未明確提及任何會導致硬分叉的協議變更。雖然有新增功能和修復，但這些並不構成硬分叉的必要條件。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.1.2 (2024-10-16 21:10:56)
```

v5.1.2 hotfix release
=====================

Prysm v5.1.1 contains an updated implementation of the beacon api streaming events endpoint. This new implementation contains a bug that can cause a panic in certain conditions. The issue is difficult to reproduce reliably and we are still trying to determine the root cause, but in the meantime we are issuing a patch that recovers from the panic to prevent the node from crashing.

This only impacts the v5.1.1 release beacon api event stream endpoint...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.1.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是針對先前版本 (v5.1.1) 中的錯誤進行的熱修復，並未引入任何重大變更或破壞性變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.1.1 (2024-10-15 20:43:30)
```

This release has a number of features and improvements. Most notably, the feature flag `--enable-experimental-state` has been flipped to "opt out" via `--disable-experimental-state`. The experimental state management design has shown significant improvements in memory usage at runtime. Updates to libp2p's gossipsub have some bandwidith stability improvements with support for IDONTWANT control messages.

⚠️ The gRPC gateway has been deprecated from Prysm in this release. If you need JSON data, ...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.1.1
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新包含了多項重大變更，包括移除 gRPC 網關和某些功能的棄用，這些變更會影響現有用戶的實作，因此需要進行升級以保持相容性。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.1.0 (2024-08-20 18:55:13)
```

This release contains 171 new changes and many of these are related to Electra! Along side the Electra changes, there are nearly 100 changes related to bug fixes, feature additions, and other improvements to Prysm. Updating to this release is recommended at your convenience.

⚠️ **Deprecation Notice: Removal of gRPC Gateway and Gateway Flag Renaming** ⚠️

In an upcoming release, we will be deprecating the gRPC gateway and renaming several associated flags. This change will result in the remova...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.1.0
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本包含171項新變更，並且有關於gRPC網關的重大變更，這可能會導致與舊版本不兼容，因此建議用戶進行升級。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.0.4 (2024-06-21 16:13:40)
```

This release has many wonderful bug fixes and improvements. Some highlights include p2p peer fix for windows users, beacon API fix for retrieving blobs older than the minimum blob retention period, and improvements to initial sync by avoiding redundant blob downloads.

Updating to this release is recommended at your earliest convenience, especially for windows users.

Review the full diff here: [v5.0.3...v5.0.4](https://github.com/prysmaticlabs/prysm/compare/v5.0.3...v5.0.4)

Added
-----

* Be...```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.0.4
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本主要是針對錯誤修正和功能改進，並未引入任何破壞性變更或強制升級的要求，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v5.0.4-rc.3: Keep only the latest value in the health channel (#14087) (2024-06-10 12:54:10)
```

* Increase health tracker channel buffer size
* keep only the latest value
* Make health test blocking as a regression test for PR #14807
* Fix new race conditions in the MockHealthClient

---

Co-authored-by: Preston Van Loon [preston@pvl.dev](mailto:preston@pvl.dev)

```

- 🔗 Link: https://github.com/prysmaticlabs/prysm/releases/tag/v5.0.4-rc.3
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤和增強功能，並未改變底層協議或共識規則，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from core-geth](https://github.com/etclabscore/core-geth/releases.atom)

### Prophasis (v1.12.20) (2024-06-10 14:53:20)
```

This release merges the v1.13.x ethereum/go-ethereum release series, through v1.13.15.

> Geth [v1.13.0](https://github.com/ethereum/go-ethereum/releases/tag/v1.13.0) is a major milestone in the lifetime of Geth, bits and bobs being in development for around 6 years now. Since a release note cannot do it justice, please see our [Geth v1.13.0 release blog post](https://blog.ethereum.org/2023/09/12/geth-v1-13-0).

This release series brought Ethereum through the Cancun fork, which established Sh...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.20
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本合併了以太坊的重大更新，並引入了許多新功能和變更，這可能會導致與以太坊的分歧，因此需要進行硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Persiphone (v1.12.19) (2024-02-05 19:56:31)
```

Fixed
-----

* Fix UPnP unwanted termination, which was causing nodes behind a NAT to be unreachable. ([#611](https://github.com/etclabscore/core-geth/pull/611))
* Fix config toml, go generate. Allowing setting the `ECBP1100` and `OverrideECBP1100Deactivate` through TOML configuration. ([#614](https://github.com/etclabscore/core-geth/pull/614))

---

Comparison with last release: [v1.12.19..v1.12.18](https://github.com/etclabscore/core-geth/compare/v1.12.18..v1.12.19)

Docker images publishe...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.19
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是修復錯誤和增強功能，並未涉及共識規則的變更，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Gaia (v1.12.18) (2024-01-09 17:11:53)
```

What's Changed
--------------

* Install [ECBP-1110 (Deactivate MESS)](https://github.com/ethereumclassic/ECIPs/blob/master/_specs/ecip-1110.md) for **Mordor** at block `10_400_000` ([#602](https://github.com/etclabscore/core-geth/pull/602))
* Avoid hitting Cloudflare DNS record quota ([#598](https://github.com/etclabscore/core-geth/pull/598))

Fixed
-----

* Fix mordor bootnode IP ([#604](https://github.com/etclabscore/core-geth/pull/604))

---

Comparison with last release: [v1.12.18..v1.12....```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.18
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新包含了對Mordor測試網的重大變更，特別是ECBP-1110的安裝，這需要所有節點在特定區塊之前進行升級，否則將無法與網絡兼容，因此這是一個硬分叉。
- 🔢 Block Number: 10400000
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Mordor
- 📅 Upgrade Deadline: 2024-01-09T17:11:53Z

### Aphrodite (v1.12.17) (2023-12-06 20:34:08)
```

⚠️ This release is a mandatory upgrade for ETC clients, it includes upcoming activation values for the Spiral hardfork, scheduled for late January 2024. This release also includes **an important fix for a miner DoS vulnerability**, where an attacker could toggle mining intermittently by broadcasting statuses with fake total difficulties. For more information, please see the blog post/disclosure [here](https://etccooperative.org/posts/2023-12-06-miner-autopause-vulnerability-disclosure-en).

Al...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.17
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本是 ETC 客戶端的強制升級，包含即將於 2024 年 1 月啟動的 Spiral hardfork 的激活值，並修復了礦工 DoS 漏洞，因此這是一個硬分叉。
- 🔢 Block Number: 19250000
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-01-31T00:00:00Z

### Real Eris (v1.12.16) (2023-11-08 22:48:18)
```

Fix a logistics issue with the latest release (v1.12.15) which, in fact, did *not* include the Mordor (Testnet) [Spiral](https://ecips.ethereumclassic.org/ECIPs/ecip-1109) activation numbers! So this release *does* *actually* have the Spiral configuration for Mordor coded. 🤦 🚀

The `master` branch has included the Spiral blocks for Mordor since merging [#571](https://github.com/etclabscore/core-geth/pull/571).

### Fixed

* Mordor Spiral activation number (`9,957,000`).
* Fixed a silent-but-...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.16
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新包含了Mordor測試網的Spiral升級激活號碼，這是一個重要的協議變更，並且需要用戶進行升級，因此這是一個硬分叉。
- 🔢 Block Number: 9957000
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Mordor
- 📅 Upgrade Deadline: None

### Eris (v1.12.15) (2023-10-26 12:22:27)
```

* Add block activation numbers for Ethereum Classic's Spiral fork for the Mordor network ([#571](https://github.com/etclabscore/core-geth/pull/571)). Specifications for this network upgrade are available in the [ECIP-1109](https://ecips.ethereumclassic.org/ECIPs/ecip-1109)

  This is expected to become active around November 7th 2023

⚠️ THIS IS A **MANDATORY** RELEASE FOR MORDOR CLIENTS\* ⚠️

\*: this release is not mandatory for mainnet clients

```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.15
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的釋出說明中提到，對於Mordor網絡的Spiral分叉，必須升級客戶端，並且有明確的激活時間，這表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Mordor
- 📅 Upgrade Deadline: 2023-11-07T00:00:00Z

### Poseidon (v1.12.14) (2023-09-21 20:50:27)
```

This release merges upstream through [ethereum/go-ethereum@v1.12.2](https://github.com/ethereum/go-ethereum/releases/v1.12.2).

What's Changed
==============

* Merge ethereum/go-ethereum release v1.12.1
* Merge ethereum/go-ethereum release v1.12.2

Highlights
==========

The list below is an abstract of noteworthy changes. For reference please consult the ethereum/go-ethereum release notes at their [original source](https://github.com/ethereum/go-ethereum/releases). Notable divergences or cha...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.14
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本不構成硬分叉，因為它沒有引入任何重大變更或強制升級。所有的更新都是向後兼容的，並且沒有改變共識規則。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Alcyone (v1.12.13) (2023-07-07 21:34:15)
```

This release merges upstream up to [ethereum/go-ethereum@v1.12.0](https://github.com/ethereum/go-ethereum/tree/v1.12.0).

What's Changed
==============

* Merge ethereum/go-ethereum release [v1.12.0](https://github.com/ethereum/go-ethereum/releases/tag/v1.12.0). [#551](https://github.com/etclabscore/core-geth/pull/551)
* Drops Kotti chain support. [#552](https://github.com/etclabscore/core-geth/pull/552)

  > for syncing with Kotti, [v1.12.12](https://github.com/etclabscore/core-geth/release...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.13
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本不包含重大變更或不相容的更新，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Ariadne (v1.12.12) (2023-05-30 14:33:09)
```

This is a security release of Core-Geth, addressing the *Ghost-128 SNaP* attack strategy described by [Paterson and Taverna](https://twitter.com/kennyog/status/1658057298634309638). See also [ETC Coop's blog post](https://etccooperative.org/posts/2023-05-15-addressing-practical-attacks-on-core-geth-synchronising-nodes-by-taverna-and-paterson-en). We encourage all users to upgrade to this version to reduce risk while synchronizing with the default `--syncmode=snap` strategy.

What's Changed
===...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.12
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本是針對Ghost-128 SNaP攻擊的安全更新，並強烈建議所有用戶升級以降低風險，這表明此版本可能會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Iris (v1.12.11) (2023-05-17 12:51:54)
```

This is a security release of Geth, addressing the *SNaP* attack strategy described by [Paterson and Taverna](https://twitter.com/kennyog/status/1658057298634309638). See also [ETC Coop's blog post](https://etccooperative.org/posts/2023-05-15-addressing-practical-attacks-on-core-geth-synchronising-nodes-by-taverna-and-paterson-en).

Merging upstream through [ethereum/go-ethereum@v1.11.5](https://github.com/ethereum/go-ethereum/tree/v1.11.5), this release also includes a security patch relate...```

- 🔗 Link: https://github.com/etclabscore/core-geth/releases/tag/v1.12.11
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本是核心 Geth 的安全更新，解決了特定的漏洞，並且包含了重要的上游合併和功能變更，這些都表明用戶必須升級以保持安全性和功能性。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from bsc](https://github.com/bnb-chain/bsc/releases.atom)

### v1.5.1-alpha (2024-12-10 02:14:59)
```

Description
-----------

v1.5.1-alpha is a maintenance release, which mainly include the code sync with [Go-Ethereum [v1.13.15, v1.14.11]](https://github.com/ethereum/go-ethereum/releases).

As it involves quite a lot of commits, needs more effort and time to verify its quality, mark it as alpha release and would not recommend to use it in product environments.

Changelog
---------

It is a quite long list, pls refer: [#2790](https://github.com/bnb-chain/bsc/pull/2790)

Assets
------

| Assets...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.5.1-alpha
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本被標記為 alpha 版本，主要是維護性更新，並且不建議在生產環境中使用。這表明它不會引入硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.5.0-alpha (2024-12-09 07:53:23)
```

Changelog
---------

Assets
------

| Assets | Sha256 Checksum |
| --- | --- |
| mainnet.zip | e9143c17e5369414fb3a569155eb5c66cee7c4395c13695b73d669a9df46fa46 |
| testnet.zip | 042a1884b00e6cd72af5c3e31c5985b9d8a78a29ccc19fb4ba660e0da1e621e7 |
| geth\_linux | 30025df1599ed3c1e7ad40787f1189ca1e46c0cac4ad7f7a1c1a573781b0a6ff |
| geth\_mac | 2630771c6ad8f072d9e1c66f67c7d33b0b3528b82f4540147ce5f8da0abb4d73 |
| geth\_windows | 9a6770a0f31c712b4655818b4f63ac22ca05abd11cf0f3e8ca2c237477ecaec3 |
| ge...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.5.0-alpha
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本 v1.5.0-alpha 沒有明確提到必須升級或重大變更，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names: testnet.zip
- 📅 Upgrade Deadline: None

### v1.4.16 (2024-11-26 09:46:54)
```

Changelog
---------

**v1.4.16** is a maintenance release, which mainly include:

* Fix a multi-DB bug, which failed to prune historical data from main db after BSC support 4844
* Add the code framework of BSC next hardfork: Pascal
* Systemcontract code cleanup, which is part of Pascal hard fork without a BEP.
* New feature: [overflowpool](https://github.com/bnb-chain/bsc/pull/2660), it tries to enhance the current TxPool to support large traffic.
* Add some tool for trouble shoot, JSTool and ...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.16
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含對未來硬分叉Pascal的代碼框架，並且明確提到與Pascal硬分叉相關的功能和改進，顯示出這是一個重要的硬分叉準備版本。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: BSC Testnet
- 📅 Upgrade Deadline: 2024-12-31T23:59:59Z

### v1.4.15 (2024-10-10 05:06:34)
```

Require Mandatory Update? No

Description
-----------

v1.4.15 is a maintenance release, which mainly has some enhancement on P2P and TxPool module, it also provides some Restful API for L2 and support customized token on BSC faucet.

Changelog
---------

### BUGFIX

* [#2680](https://github.com/bnb-chain/bsc/pull/2680) txpool: apply miner's gasceil to txpool
* [#2688](https://github.com/bnb-chain/bsc/pull/2688) txpool: set default GasCeil from 30M to 0
* [#2696](https://github.com/bnb-chain/b...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.15
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本為維護版本，主要進行了增強和錯誤修復，並未提及任何重大變更或強制更新，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names: testnet
- 📅 Upgrade Deadline: None

### v1.4.14 (2024-09-05 05:18:25)
```

**Important Announcement:**

HashSchema&LevelDB mode will be discontinued after September 30, 2024, will be replaced by PathSchema&PebbleDB mode

If you are still running with HashSchema or LevelDB, you need to reinstall your node with the [latest bsc-snapshot](https://github.com/bnb-chain/bsc-snapshots).

How to check the running mode and the steps to do the migration, pls refer: [bnb-chain/bsc-snapshots#379](https://github.com/bnb-chain/bsc-snapshots/issues/379).

Notice
------

Requir...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.14
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.4.14 是 BSC 主網的硬分叉，名為 Bohr，並且需要強制更新。更新中包含了多個 BEP，並且明確指出 HashSchema 和 LevelDB 模式將被淘汰，這些都表明了這是一個重要的協議變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-09-26T02:20:00Z

### v1.4.13 (2024-08-15 03:25:53)
```

**Important Announcement:**

HashSchema&LevelDB mode will be discontinued after September 30, 2024, will be replaced by PathSchema&PebbleDB mode

If you are still running with HashSchema or LevelDB, you need to reinstall your node with the [latest bsc-snapshot](https://github.com/bnb-chain/bsc-snapshots).

How to check the running mode and the steps to do the migration, pls refer: [bnb-chain/bsc-snapshots#379](https://github.com/bnb-chain/bsc-snapshots/issues/379).

Notice
------

Requir...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.13
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.4.13 是 BSC 測試網的硬分叉版本，並且明確要求測試網用戶進行強制更新。主網的更新時間尚未確定，但預計在 2024 年 9 月稍後進行。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: BSC Testnet
- 📅 Upgrade Deadline: 2024-09-30T00:00:00Z

### v1.4.12 (2024-07-24 06:14:51)
```

Notice
------

Mandatory Update: **No**

This is a maintenance release, which includes some bug fix of: `--pruneancient`, `issues of force kill`, `multi-database`, `snapshot prune-state`. And also has some improvements on `vote`, `minor`, `mev`, `freezer`

Changelog
---------

### BUGFIX

* [#2557](https://github.com/bnb-chain/bsc/pull/2557) fix: fix state inspect error after pruned state
* [#2562](https://github.com/bnb-chain/bsc/pull/2562) fix: delete unexpected block
* [#2566](https://githu...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.12
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.4.12 是一個維護版本，包含了一些錯誤修正和改進，並且明確指出不是強制更新，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.4.11 (2024-07-10 15:35:35)
```

Notice
------

Mandatory Update: **Yes**

This is a hardfork release target to resolve a staking reward distribution issue on BSC testnet. This upgrade, known as the "Haber Fix" upgrade, is scheduled to take place on July 3, 2024, at 06:06:28 GMT. All clients on BSC testnet are encouraged to upgrade to the latest version.

*Optional for the client running on mainnet.*

Changelog
---------

### BUGFIX

* [#2534](https://github.com/bnb-chain/bsc/pull/2534) fix: nil pointer when clear simulating ...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.11
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 這是一個強制更新，針對BSC測試網的質押獎勵分配問題進行修復，並且有明確的升級時間表，這些都表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: BSC testnet
- 📅 Upgrade Deadline: 2024-07-03T06:06:28Z

### v1.4.10 (2024-06-21 08:30:53)
```

**Notice:**

v1.4.10 solved the ["BAD BLOCK"](https://github.com/bnb-chain/bsc/issues/2522) issue after Haber hard fork, pls use this version if your node has the BAD BLOCK issue.

Description
-----------

Mandatory Update: **No(but strongly recommended!)**

Latest Mandatory Update: **[v1.4.8](https://github.com/bnb-chain/bsc/releases/v1.4.8)**

v1.4.10 is a maintenance release, which has several improvements and fixes:

* improve: performance, MEV-API, less-reorg
* fix: ethapi, UT failure...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.10
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.4.10 不是強制升級，且沒有引入任何不相容的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.4.9 (2024-06-18 07:28:42)
```

Description
-----------

Mandatory Update: **No**

Latest Mandatory Update: **[v1.4.8](https://github.com/bnb-chain/bsc/releases/v1.4.8)**

v1.4.9 is a maintenance release, which mainly addressed some issues about: **prune-block**, **multi-database** and **MEV**

There is no compatible change, to upgrade to v1.4.9 from v1.4.x, simply replace the binary should work.

Changelog
---------

### FEATURE

* [#2463](https://github.com/bnb-chain/bsc/pull/2463) utils: add check\_blobtx.js
* [#2470]...```

- 🔗 Link: https://github.com/bnb-chain/bsc/releases/tag/v1.4.9
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本 v1.4.9 是一個維護版本，並未引入任何不相容的變更，且明確指出不需要強制升級，因此不屬於硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from nitro](https://github.com/OffchainLabs/nitro/releases.atom)

### Arbitrum Nitro v3.3.0 Release Candidate 2 (2024-12-09 15:09:42)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.3.0-rc.2-d07d7a4`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.3.0-rc.2
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 這個版本的釋出並未明確表示為硬分叉，但包含了重要的變更，可能會影響兼容性，因此建議用戶升級以獲得最佳性能。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.3.0 Release Candidate 1 (2024-11-08 16:39:50)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.3.0-rc.1-a81da40`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.3.0-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是 Arbitrum Nitro 的候選版本，包含多項改進和配置變更，但未提及任何會導致硬分叉的重大變更。所有變更均為增強功能，並未影響區塊鏈的基本協議，因此這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.2.1 (2024-09-24 15:38:43)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.2.1-d81324d`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `offch...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.2.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的釋出並未提及任何重大變更或強制升級的要求，且主要是對現有功能的增強，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.2.0 (2024-09-24 17:49:35)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.2.0-f847be0`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `offch...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.2.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本包含安全修復，並且需要升級到 ArbOS 32，這是為了確保網絡的安全性和功能性。Arbitrum 安全委員會計劃執行緊急行動以啟用 ArbOS 32，因此升級是必須的。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-09-30T00:00:00Z

### Arbitrum Nitro Consensus v32 (2024-09-24 15:09:42)
```

This release signifies a WASM fraud proof consensus version, and is not a good version to run a node on
-------------------------------------------------------------------------------------------------------

**WAVM Module Root**: 0x184884e1eb9fefdc158f6c8ac912bb183bf3cf83f0090317e0bc4ac5860baa39

This consensus release supports ArbOS 32.

**Full Changelog**: [consensus-v31...consensus-v32](https://github.com/OffchainLabs/nitro/compare/consensus-v31...consensus-v32)

```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/consensus-v32
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本標示為WASM欺詐證明共識版本，並且不適合運行節點，這表明存在重大變更，可能導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.2.0 Binary Release (2024-09-23 20:47:50)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.2.0-f847be0`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `offch...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.2.0-binary-release
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含安全修復和對 ArbOS 32 的升級，Arbitrum 安全委員會計劃在未來幾天內執行緊急行動以啟用 ArbOS 32，因此升級是必需的。這表明所有節點都必須更新以保持網絡的安全性和功能性。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-09-30T23:59:59Z

### Arbitrum Nitro Consensus v32 Binary Release (2024-09-23 20:45:37)
```

**WAVM Module Root**: 0x184884e1eb9fefdc158f6c8ac912bb183bf3cf83f0090317e0bc4ac5860baa39

This consensus release supports ArbOS 32.

```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/consensus-v32-binary-release
- 🔴 Hardfork: yes
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本的發布涉及共識機制的重大變更，並支持 ArbOS 32，這可能導致不向後兼容的情況，因此推測這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.1.3 Release Candidate 2 (2024-09-16 16:57:59)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.1.3-rc.2-4483e77`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.1.3-rc.2
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含重大變更，包括穩定性改進和新功能，這些都可能影響網絡運作，因此需要用戶升級其節點以保持兼容性。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v3.1.3-rc.1 (2024-09-03 18:45:34)
```

Arbitrum Nitro v3.1.3 Release Candidate 1

```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.1.3-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為釋出候選版本，通常不會包含重大變更或強制升級的要求，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Arbitrum Nitro v3.1.2 (2024-08-27 20:06:29)
```

This release is available as a Docker image on Docker Hub at `offchainlabs/nitro-node:v3.1.2-309340a`

This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: `/usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines`

If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image `offch...```

- 🔗 Link: https://github.com/OffchainLabs/nitro/releases/tag/v3.1.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本主要是修復錯誤和增強部署，而不是對區塊鏈協議進行根本性改變，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from go-ethereum](https://github.com/OffchainLabs/go-ethereum/releases.atom)

### v1.13.3 (2023-10-12 11:36:49)
```

params: release Geth v.1.13.3

```

- 🔗 Link: https://github.com/OffchainLabs/go-ethereum/releases/tag/v1.13.3
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的釋出說明中並未提及任何硬分叉的相關內容，且沒有強制升級的要求，因此可以推斷這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Go-Ethereum Nitro v2.0.2 (2022-09-08 18:40:15)
```No content.```

- 🔗 Link: https://github.com/OffchainLabs/go-ethereum/releases/tag/v2.0.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的發布沒有提供任何具體的內容或重大變更，且沒有提到必須升級的要求，因此可以推斷這不是一次硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from web3signer](https://github.com/Consensys/web3signer/releases.atom)

### 24.12.0 (2024-12-06 01:00:51)
```

This release contains various libraries updates, including Teku libraries, which brings changes for new test networks and Prague-Electra fork. and is recommended for all users. There are no database migration scripts changes in this release.

Highlights
----------

### Breaking Changes

* Java 21 is required to build and run Web3Signer. This may affect users who use Java 17 to directly run Web3Signer binaries. The docker image was already using Java 21 for runtime in past releases.
* Filecoin ...```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.12.0
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本包含對Electra分叉的支持，並且有多個重大變更，這表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.12.0-RC1 (2024-12-02 09:45:33)
```

Pre-release 24.12.0-RC1

```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.12.0-RC1
- 🟢 Hardfork: no
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本為預發版本，並未明確提及必須升級或硬分叉，因此推測此版本不是硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.6.0 (2024-06-12 01:05:40)
```

This release contains various libraries updates and is recommended for all users.

Highlights
----------

### Upcoming Breaking Changes

* This is the last Web3Signer release to use Java 17. Web3Signer will start mandating Java 21 for build and runtime after

  this release. The Web3Signer docker image will also use Java 21, however, binary distributions (.tar.gz/.zip) will

  require Java 21 to be available on the host machine.
* This is the last Web3Signer release to use the "filecoi...```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.6.0
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本包含重大變更，但不構成區塊鏈意義上的硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.6.0-RC1 (2024-06-06 23:52:14)
```

Release 24.6.0-RC1

```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.6.0-RC1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 根據釋放說明，版本 24.6.0-RC1 沒有明確提到必須升級，且內容未顯示有重大變更，因此不認為這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.2.0 (2024-02-19 07:56:43)
```

This is a required update for Mainnet users containing the configuration for the Deneb upgrade on March 13th. This update is required for Gnosis Deneb network upgrade on March 11th. For all other networks, this update is optional.

Ethereum Mainnet configuration with Deneb fork scheduled for epoch 269568 (March 13, 2024, 13:55:35 UTC)

Gnosis configuration with Deneb fork scheduled for epoch 889856 (March 11, 2024, 18:30:20 UTC)

Highlights
----------

### Upcoming Breaking Changes

* --Xwor...```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.2.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本包含對以太坊主網的強制更新，並且有計劃的Deneb升級，這些都表明這是一個硬分叉。
- 🔢 Block Number: 269568
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Gnosis
- 📅 Upgrade Deadline: 2024-03-11T18:30:20Z

### 24.2.0-RC1 (2024-02-16 05:12:00)
```

Release 24.2.0-RC1

```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.2.0-RC1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本 24.2.0-RC1 沒有明確提到必須升級，且沒有提供測試網或特定區塊號，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.1.1 (2024-01-25 07:24:42)
```

24.1.1
------

This is an optional release for mainnet Ethereum and it includes the updated network configuration for the Sepolia, Holesky and Chiado Deneb forks.

* Sepolia is scheduled for 2024-01-30 22:51:12 UTC
* Chiado is scheduled for 2024-01-31 18:15:40 UTC
* Holesky is scheduled for 2024-02-07 11:34:24 UTC

### Features Added

* Add Deneb configuration for Sepolia, Holesky and Chiado forks

---

### Downloads

| File | Checksum (sha256) |
| --- | --- |
| [web3signer.tar.gz](https://art...```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.1.1
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 這次版本更新是針對以太坊即將到來的分叉進行的，雖然標記為可選，但實際上對於保持與新網絡配置的兼容性至關重要，因此可以視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names: Sepolia, Holesky, Chiado
- 📅 Upgrade Deadline: 2024-01-30T22:51:12Z

### 24.1.1-RC1 (2024-01-25 00:02:45)
```

Release 24.1.1-RC1

```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.1.1-RC1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 根據釋放說明，版本 24.1.1-RC1 並未明確提及必須升級，且缺乏重大變更的跡象，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### 24.1.0 (2024-01-11 01:56:31)
```

24.1.0
------

This is an optional release for mainnet Ethereum, required for the upcoming Goerli Deneb fork.

The Goerli upgrade is scheduled on 2024-01-17 06:32:00 UTC (timestamp 1705473120).

### Bugs fixed

* Update reactor-netty-http to fix [CVE-2023-34062](https://github.com/advisories/GHSA-xjhv-p3fv-x24r "CVE-2023-34062")

### Features Added

* Add Deneb configuration for Goerli [#960](https://github.com/Consensys/web3signer/pull/960)

---

### Downloads

| File | Checksum (sha256) |
| ...```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.1.0
- 🔴 Hardfork: yes
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本是針對即將到來的 Goerli Deneb 升級所需的，雖然標記為可選，但為了在升級後保持網絡的兼容性，使用者必須升級。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Goerli
- 📅 Upgrade Deadline: 2024-01-17T06:32:00Z

### 24.1.0-RC1 (2024-01-10 03:02:31)
```

Release 24.1.0-RC1

```

- 🔗 Link: https://github.com/Consensys/web3signer/releases/tag/24.1.0-RC1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本 24.1.0-RC1 沒有明確指出必須升級或有重大變更，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Arbitrum Status - Incident history](https://status.arbitrum.io/history.rss)

### NOVA - Arbiscan outage (2024-12-02 01:35:05)
```

Dec  2, 01:35:05 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Dec  2, 04:41:07 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm46cyla1008khjpywbsuuo9o
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 根據報告，NOVA - Arbiscan 的故障是由於服務中斷，並且已經恢復正常運行。這表明底層區塊鏈沒有出現重大問題，因此不需要進行硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-11-25 07:04:04)
```

Nov  25, 07:11:03 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

Nov  25, 07:04:04 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm3womp5l0023hk6d8ezhposg
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於 Arbiscan 的暫時性技術問題造成的，並不涉及區塊鏈協議的根本變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-11-12 08:17:05)
```

Nov  12, 08:17:05 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Nov  12, 08:28:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm3e6iiua00g6nwkjw37alece
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: ARB1 - Arbiscan 的故障是由於服務中斷，而非區塊鏈的硬分叉。故障持續時間短，且已經恢復正常，這表明這是一個操作性問題，而不是協議的變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-11-06 11:47:05)
```

Nov  6, 11:47:05 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Nov  6, 11:57:53 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm35tdh5r002y12i0u7qq1cif
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 這次事件是由於 Arbiscan 的暫時性故障，並不涉及任何協議的變更或硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-11-06 11:47:03)
```

Nov  6, 11:47:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Nov  6, 11:58:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm35tdfjo002q12i09hmadued
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是服務中斷，並不表示區塊鏈的硬分叉或協議升級。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-11-01 00:44:06)
```

Nov  1, 00:44:06 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Nov  1, 00:47:06 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2y0hly7001110ilwg6vmnhw
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 這次事件是由於 Arbiscan 的暫時性故障，並不涉及任何硬分叉或協議變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-10-30 09:02:04)
```

Oct  30, 09:02:04 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Oct  30, 09:06:05 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2vneado000gel11g8yz3olp
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於 Arbiscan 的暫時無法訪問，並不涉及任何區塊鏈協議的根本變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-10-28 07:08:02)
```

Oct  28, 07:08:02 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Oct  28, 07:17:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2sofydg002tzcv8wzxgwiud
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於服務中斷造成的，並不涉及任何區塊鏈的硬分叉或重大變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-10-26 09:34:03)
```

Oct  26, 09:34:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Oct  26, 09:37:05 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2pys10b00uxrvn2oxs93y6u
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於Arbiscan的服務中斷，並不涉及區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-10-21 07:09:04)
```

Oct  21, 07:09:04 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Oct  21, 07:11:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2ioebay002l132cjmscla9n
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於Arbiscan的服務中斷，並不涉及區塊鏈協議的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-10-18 08:07:07)
```

Oct  18, 08:07:07 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Oct  18, 08:14:06 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm2eg5ehe004izgngoct9glh2
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 這次事件是 Arbiscan 的暫時服務中斷，並不涉及任何區塊鏈協議的變更，因此不算作硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-30 07:17:03)
```

Sep  30, 07:17:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  30, 07:22:03 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm1oofp6x03g1yeasa6wk5mhu
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的服務中斷，並不涉及區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-23 07:09:03)
```

Sep  23, 07:09:05 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

Sep  23, 07:09:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm1eo2fnu025xlx5wpjgwo0kt
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的服務中斷，並不涉及區塊鏈協議的變更，因此不是硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-09-20 08:07:06)
```

Sep  20, 08:13:05 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

Sep  20, 08:07:06 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm1aftj8800c5h67typppggpi
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件與硬分叉無關，因為它僅涉及 Arbiscan 的服務中斷，並未提及任何區塊鏈的重大變更或升級。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-09-17 15:19:45)
```

Sep  17, 15:19:45 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  17, 15:22:39 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm16kyd3v000m22twuz8xlw50
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: NOVA - Arbiscan 的故障是由於服務暫時無法訪問，並不表示區塊鏈協議的重大變更或硬分叉。故障已迅速解決，且沒有提及任何硬分叉或升級的計劃，因此可以合理地推斷這不是一次硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-17 15:17:29)
```

Sep  17, 15:17:29 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  17, 15:22:14 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm16kvgkq01zhh5sfkrvzuk1x
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的暫時故障，而不是區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-17 15:07:11)
```

Sep  17, 15:15:38 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

Sep  17, 15:07:11 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm16ki7rd00ai4wjvg0951mex
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的暫時性服務中斷，並不涉及區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-13 06:41:05)
```

Sep  13, 06:41:05 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  13, 06:43:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm10cnye401bhl3s62s8kh3dn
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於Arbiscan服務的暫時性故障，而非區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-08 03:38:05)
```

Sep  8, 03:38:05 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  8, 08:11:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm0t0xczh00zuomc1g66p1bvj
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: ARB1 - Arbiscan 的故障是由於服務中斷，而非區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-09-02 07:09:03)
```

Sep  2, 07:09:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Sep  2, 07:19:03 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm0kntk2b007mlqzj4izfoqx6
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的暫時無法訪問，並不涉及區塊鏈協議的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### NOVA - Arbiscan outage (2024-08-30 08:13:05)
```

Aug  30, 08:13:05 GMT+0
**Investigating** -
NOVA - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Aug  30, 08:17:05 GMT+0
**Resolved** -
NOVA - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm0gfsc670001wpjgkfijp6ai
- 🟢 Hardfork: no
- 📊 Confidence: 95.0%
- 📝 Explanation: 這次事件是由於 Arbiscan 的服務中斷，並不涉及任何區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-08-24 16:13:27)
```

Aug  24, 16:13:27 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Aug  24, 16:21:26 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm08cazfd00lzmqcmj4e2lurs
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是 Arbiscan 的暫時服務中斷，並不表示區塊鏈協議的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-08-24 16:07:03)
```

Aug  24, 16:08:27 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

Aug  24, 16:07:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm08c2r4e004uxa4es2i2qgm2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此事件是由於 Arbiscan 的暫時性服務中斷，而非區塊鏈協議的變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-08-24 10:45:03)
```

Aug  24, 12:45:05 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

Aug  24, 10:45:03 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/cm080ko2b008sy90hx0pxczlt
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: ARB1 - Arbiscan 的故障是服務中斷，而不是區塊鏈協議的根本變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### ARB1 - Arbiscan outage (2024-08-12 07:07:05)
```

Aug  12, 07:07:05 GMT+0
**Investigating** -
ARB1 - Arbiscan cannot be accessed at the moment. More details, including information about planned outages, can be found on the [Arbiscan status page](https://arbiscan.freshstatus.io/). This incident was created by an automated monitoring service..

Aug  12, 07:08:04 GMT+0
**Resolved** -
ARB1 - Arbiscan is now operational! This update was created by an automated monitoring service..

```

- 🔗 Link: https://status.arbitrum.io/incident/clzqni4gw22955jdoe9d43m4fs
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: ARB1 - Arbiscan 的故障是由於服務暫時無法訪問，並不涉及任何區塊鏈協議的變更或升級，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from coreth](https://github.com/ava-labs/coreth/releases.atom)

### v0.14.0 (2024-12-10 19:04:58)
```

Note the minor version change reflects upgrading past avalanchego v1.12.0 as it corresponds with the Etna upgrade.

The necessary code for the upgrade is already included in the avalanchego release.

What's Changed
--------------

* remove CALLEX, BALANCEMC by [@darioush](https://github.com/darioush) in [#651](https://github.com/ava-labs/coreth/pull/651)
* remove pre-AP2 handling of genesis contract by [@darioush](https://github.com/darioush) in [#658](https://github.com/ava-labs/coreth/pull...```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.14.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新是小版本變更，並且沒有提及任何需要硬分叉的重大變更，因此可以推斷這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.9-rc.2-encapsulate-signer: Encapsulate Signer (#693) (2024-12-04 23:26:41)
```

* Remove the bls dependency

---

Co-authored-by: Darioush Jalali [darioush.jalali@avalabs.org](mailto:darioush.jalali@avalabs.org)

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.9-rc.2-encapsulate-signer
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本不構成硬分叉，因為它沒有強制升級的要求，也沒有引入會導致所有節點必須升級的重大變更。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.9-rc.1 (2024-11-15 21:01:15)
```

bump avago to v1.11.13-rc.0 ([#688](https://github.com/ava-labs/coreth/pull/688))

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.9-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本更新僅為依賴項的版本提升，並未引入任何共識或協議的重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.9-rc.0 (2024-11-13 22:42:19)
```

sync subnet-evm to 981830ed + avalanchego v1.12.0-initial-poc.9 ([#686](https://github.com/ava-labs/coreth/pull/686))

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.9-rc.0
- 🟡 Hardfork: unknown
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本的更新涉及到重要的協議變更，雖然沒有明確標示為「必須升級」，但根據過去的經驗，這類更新可能會導致硬分叉，因此存在硬分叉的可能性。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.8 (2024-09-18 22:29:20)
```

What's Changed
--------------

* eupgrade: lowering the base fee by [@darioush](https://github.com/darioush) in [#604](https://github.com/ava-labs/coreth/pull/604)
* eupgrade/cancun: verify no blobs in header by [@darioush](https://github.com/darioush) in [#611](https://github.com/ava-labs/coreth/pull/611)
* enables cancun at EUpgrade by [@darioush](https://github.com/darioush) in [#610](https://github.com/ava-labs/coreth/pull/610)
* nits, update comments by [@darioush](https://github.com/dari...```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.8
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本的更新包含多項改進和修復，但並未明確要求用戶必須升級，且沒有改變共識規則，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.8-fix-genesis-upgrade (2024-08-08 15:14:52)
```

Allow local chains to specify their own config ([#627](https://github.com/ava-labs/coreth/pull/627))

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.8-fix-genesis-upgrade
- 🟡 Hardfork: unknown
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本的更新允許本地鏈指定自己的配置，這可能會影響共識機制或節點之間的互動。雖然這些變更可能需要升級以保持兼容性，但沒有明確的'必須升級'說明，因此是否會導致硬分叉仍不確定。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### remove-crosschain-coreth (2024-08-08 16:08:39)
```

remove cross-chain handlers

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/remove-crosschain-coreth
- 🔴 Hardfork: yes
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本移除了跨鏈處理程序，這可能會導致協議的重大變更，雖然沒有明確提到必須升級，但這樣的變更通常會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.7-acp-118-handlers (2024-08-07 14:07:06)
```

Supports ACP-118 messages (code sync from subnet-evm) ([#624](https://github.com/ava-labs/coreth/pull/624))

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.7-acp-118-handlers
- 🟡 Hardfork: unknown
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本 v0.13.7-acp-118-handlers 引入了對 ACP-118 消息的支持，這可能會導致共識或交易處理的重大變化。雖然沒有明確的 '必須升級' 指令，但這樣的變更通常會導致硬分叉的可能性。因此，這次升級可能是硬分叉，但不確定性仍然存在。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### with-avalanchego-test-pkg (2024-08-01 12:39:01)
```

The introduction of `*test` packages in [ava-labs/avalanchego#3238](https://github.com/ava-labs/avalanchego/pull/3238) bre…

```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/with-avalanchego-test-pkg
- 🟡 Hardfork: unknown
- 📊 Confidence: 70.0%
- 📝 Explanation: 此版本引入了新的 *test 套件，可能會導致硬分叉，但沒有明確的 '必須升級' 指示，因此可能不是強制性的。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v0.13.7 (2024-07-23 19:31:54)
```

What's Changed
--------------

* Update to latest p2p API by [@joshua-kim](https://github.com/joshua-kim) in [#594](https://github.com/ava-labs/coreth/pull/594)
* bump avalanchego to v1.11.10-rc.0 by [@ceyonur](https://github.com/ceyonur) in [#596](https://github.com/ava-labs/coreth/pull/596)
* Fix VM.GetBlockIDAtHeight by [@StephenButtolph](https://github.com/StephenButtolph) in [#595](https://github.com/ava-labs/coreth/pull/595)
* [ci] Add actionlint job by [@marun](https://github.com/marun)...```

- 🔗 Link: https://github.com/ava-labs/coreth/releases/tag/v0.13.7
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本更新包含多項改進和修復，但未提及任何重大變更或強制升級，顯示這不是一次硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

## [Release notes from mev-boost](https://github.com/flashbots/mev-boost/releases.atom)

### v1.8.1 (2024-09-02 09:37:42)
```

v1.8.1

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 根據釋放說明，v1.8.1版本沒有提到任何強制升級或重大變更，因此這不是一次硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8.0 (2024-08-28 14:05:23)
```

v1.8.0

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8.0
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 根據釋放說明，v1.8.0 版本沒有提到任何強制升級或重大變更，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8 (2024-08-29 14:13:59)
```

What's changed
==============

MEV-Boost v1.8 includes two noteworthy (albeit minor) changes, and a bit of cleanup and dependency updates.

✨ Noteworthy changes
--------------------

* Add request start time metrics to request header field by [@bhakiyakalimuthu](https://github.com/bhakiyakalimuthu) in [#647](https://github.com/flashbots/mev-boost/pull/647)
* Remove capella types by [@avalonche](https://github.com/avalonche) in [#650](https://github.com/flashbots/mev-boost/pull/650)

🏗️ Cleanup...```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: MEV-Boost v1.8 的更新主要是小幅度的改進和清理，並未引入任何破壞性變更或協議改動，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8-rc4 (2024-08-16 13:33:25)
```

What's Changed
--------------

* Remove auction transcript code by [@jtraglia](https://github.com/jtraglia) in [#629](https://github.com/flashbots/mev-boost/pull/629)
* common: simplify floatToEth by [@MariusVanDerWijden](https://github.com/MariusVanDerWijden) in [#639](https://github.com/flashbots/mev-boost/pull/639)
* cli: refactor sanitizeMinBid by [@MariusVanDerWijden](https://github.com/MariusVanDerWijden) in [#641](https://github.com/flashbots/mev-boost/pull/641)
* server: move mock rela...```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8-rc4
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是增強和修復，並未改變區塊鏈的共識規則，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8-rc3 (2024-08-12 05:55:31)
```

v1.8-rc3

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8-rc3
- 🟢 Hardfork: no
- 📊 Confidence: 70.0%
- 📝 Explanation: 根據目前的資訊，v1.8-rc3版本的釋出說明並未明確指出有硬分叉的情況，且缺乏關於必須升級的具體說明，因此推測這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8-rc2 (2024-08-12 05:53:33)
```

v1.8-rc2

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8-rc2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.8-rc2 沒有明確提到必須升級或重大變更，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.8-rc1 (2024-08-12 05:49:57)
```

v1.8-rc1

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.8-rc1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 根據釋出說明，v1.8-rc1 並未明確要求升級，且未提及任何重大變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.7.1 (2024-02-28 08:37:36)
```

v1.7.1

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.7.1
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.7.1 的釋出說明中並未提及任何重大變更或強制升級的要求，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.7.0 (2024-02-27 05:08:38)
```

v1.7.0

```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.7.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.7.0 沒有顯示出任何強制升級或重大變更的跡象，因此不被視為硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.7 (2024-02-27 22:18:24)
```

What's Changed
==============

Deneb ready release for mainnet. **Required upgrade** for upcoming mainnet dencun fork on [March 13 13:55:35 UTC](https://github.com/ethereum/consensus-specs/pull/3597).

If building from source please upgrade to the [latest stable go version](https://go.dev/dl/) (1.22.0)

Noteworthy Changes
------------------

* Adding Deneb support and types in [#553](https://github.com/flashbots/mev-boost/pull/553)
* Adding holesky network support in [#585](https://github.com/...```

- 🔗 Link: https://github.com/flashbots/mev-boost/releases/tag/v1.7
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本的發布是必須升級的，因為它與即將到來的主網dencun硬分叉兼容，並且包含了重要的變更和更新。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-03-13T13:55:35Z

## [Release notes from avalanchego](https://github.com/ava-labs/avalanchego/releases.atom)

### v1.12.0-config-pebble-sync (2024-12-10 15:42:27)
```

move sync to cfg

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0-config-pebble-sync
- 🔴 Hardfork: yes
- 📊 Confidence: 85.0%
- 📝 Explanation: 此版本的更新涉及同步配置的重大變更，可能會導致網絡不穩定，並需要所有節點進行升級，因此預測會出現硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Etna - Reinventing Subnets (2024-12-02 22:41:44)
```

This upgrade consists of the following Avalanche Community Proposals (ACPs):

* [ACP-77](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/77-reinventing-subnets/README.md) Reinventing Subnets
* [ACP-103](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/103-dynamic-fees/README.md) Add Dynamic Fees to the P-Chain
* [ACP-118](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/118-warp-signature-request/README.md) Warp Signature Interface Standard
* [ACP-125](https:/...```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0
- 🔴 Hardfork: yes
- 📊 Confidence: 95.0%
- 📝 Explanation: 此版本的升級包含多個重大的社區提案，這些提案將導致協議的根本變化，並且升級後的節點必須在特定截止日期之前進行升級，否則將無法繼續參與網絡，這些都表明這是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: 2024-12-16T17:00:00Z

### v1.12.0-rc.1 (2024-12-02 04:05:39)
```

Merge branch 'master' into update-versions-v1.12.0

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本的更新並未明確提及硬分叉，且沒有顯示出任何破壞性變更，因此推測這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.12.0-rc.0 (2024-12-02 03:24:53)
```

Update versions for v1.12.0

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0-rc.0
- 🟡 Hardfork: unknown
- 📊 Confidence: 50.0%
- 📝 Explanation: 此版本更新的內容並未明確指出是否為硬分叉，因為更新可能是增量性的，而非根本性的改變。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### Etna - Reinventing Subnets - Fuji Pre-Release (2024-11-19 02:31:48)
```

**Please note that this release is unable to run mainnet - and will display "mainnet is not supported" if attempted to run with a mainnet configuration.**

This upgrade consists of the following Avalanche Community Proposals (ACPs):

* [ACP-77](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/77-reinventing-subnets/README.md) Reinventing Subnets
* [ACP-103](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/103-dynamic-fees/README.md) Add Dynamic Fees to the P-Chain
* [ACP-...```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0-fuji
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為測試網的預發布版本，並不會影響主網的運行，且不需要進行共識規則的改變，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: True
- 🌐 Testnet Names: Fuji
- 📅 Upgrade Deadline: 2024-11-25T11:00:00-05:00

### Durango.13 - Etna Compatible (2024-11-19 00:09:04)
```

This version is backwards compatible to [v1.11.0](https://github.com/ava-labs/avalanchego/releases/tag/v1.11.0). It is optional, but encouraged.

The plugin version is updated to `38` all plugins must update to be compatible.

### APIs

* Added `platform.getL1Validator`
* Added `platform.getProposedHeight`
* Updated `platform.getValidatorsAt` to accept `"proposed"` as valid `height` input

### Configs

* Added P-chain configs
  + `"l1-weights-cache-size"`
  + `"l1-inactive-validators-cache-siz...```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.11.13
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本為可選升級，並且向下相容於先前版本，並未強制要求用戶升級，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.11.13-rc.2 (2024-11-18 15:18:32)
```

Merge branch 'master' into update-versions-v1.11.13

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.11.13-rc.2
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.11.13-rc.2 的更新內容僅為合併主分支，並未提及任何重大變更或硬分叉，因此判斷為非硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.11.13-rc.1 (2024-11-15 21:15:51)
```

Update coreth

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.11.13-rc.1
- 🟢 Hardfork: no
- 📊 Confidence: 80.0%
- 📝 Explanation: 此版本更新僅為核心組件的更新，並未提及任何強制升級或重大變更，因此不會導致硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.11.13-rc.0: Add "proposed" optional flag to `getValidatorsAt` (#3531) (2024-11-15 20:06:55)
```

Signed-off-by: Ian Suvak [ian.suvak@avalabs.org](mailto:ian.suvak@avalabs.org)

Co-authored-by: Stephen Buttolph [stephen@avalabs.org](mailto:stephen@avalabs.org)

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.11.13-rc.0
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本 v1.11.13-rc.0 僅添加了一個可選標誌，並未引入任何破壞性變更，因此不構成硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None

### v1.12.0-initial-poc.9 (2024-11-13 19:21:04)
```

Add Etna P-chain metrics ([#3458](https://github.com/ava-labs/avalanchego/pull/3458))

```

- 🔗 Link: https://github.com/ava-labs/avalanchego/releases/tag/v1.12.0-initial-poc.9
- 🟢 Hardfork: no
- 📊 Confidence: 90.0%
- 📝 Explanation: 此版本的更新主要是增加了P鏈的指標，並未顯示出任何需要進行硬分叉的重大變更。此外，沒有提到必須升級的要求，因此可以推斷這不是一個硬分叉。
- 🔢 Block Number: None
- ⬆️ Must Upgrade: False
- 🌐 Testnet Names:
- 📅 Upgrade Deadline: None
