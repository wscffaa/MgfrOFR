# Symmetry/MDPI 参考文献逐条核对汇总

原始文件：`references(1).bib`  
修正文件：`references_symmetry_corrected.bib`  
核对日期：2026-05-14  
总条目数：50

## 处理原则

- 保留所有原始 BibTeX key，避免正文中已有的 `\cite{...}` 失效。
- 按 Symmetry/MDPI 的 LaTeX 投稿习惯，输出文件名后缀改为 `_symmetry_corrected`，但扩展名保留 `.bib`，保证 BibTeX 可直接读取。
- 优先按官方论文页面、出版社页面、NeurIPS/PMLR/CVF/IEEE/ACM/AAAI/ScienceDirect/Springer 等可核查来源修正题名、作者、年份、会议/期刊、卷期、页码、DOI/URL。
- 对软件/在线项目类条目按 `@misc + url + Accessed on ...` 处理。

## 结构检查

- 条目数：50
- 重复 key：0
- 花括号平衡：通过
- BibTeX 解析检查：通过；`plain.bst` 测试解析无 warning

## 主要实质性修正

| Key | 修正内容 |
|---|---|
| `chan2021basicvsr` | 页码由 `4945--4954` 修正为 `4947--4956`；会议条目规范化。 |
| `chan2022basicvsrpp` | 页码由 `5962--5971` 修正为 `5972--5981`；会议条目规范化。 |
| `liang2024vrt` | 作者 `Cao, Jingzhang` 修正为 `Cao, Jiezhang`。 |
| `liang2022rvrt` | 增加 NeurIPS 卷号 `35`。 |
| `zheng2023diffkendall` | 原作者列表错误；修正为 `Kaipeng Zheng, Huishuai Zhang, Weiran Huang`；补充 NeurIPS 卷号 `36`；页码修正为 `49403--49415`。 |
| `kendall1938measure` | DOI 由 JSTOR DOI 规范为 Biometrika/OUP DOI：`10.1093/biomet/30.1-2.81`；期号规范为 `1--2`。 |
| `iizuka2019deepremaster` | 增加 ACM TOG article number `176` 和 `numpages = {13}`。 |
| `li2023shiftnet` | 原作者列表错误；修正为 CVPR 官方作者列表。 |
| `liu2024vmamba` | 作者列表、NeurIPS 卷号、页码均修正；页码修正为 `103031--103063`。 |
| `wang2018mgn` | 作者名由 `Guansong Wang`/`Yufei Yuan` 修正为 `Guanshuo Wang`/`Yufeng Yuan`。 |
| `ding2020dists` | 期号由 `9` 修正为 `5`。 |
| `tran2025vsrm` | 作者 BibTeX 解析形式修正为 `Hung, Dao Duy`；删除无法在 CVF 官方条目中确认的 DOI。 |
| `yu2024supir` | 补充 CVPR DOI：`10.1109/CVPR52733.2024.02425`。 |
| `wu2024seesr` | 补充 CVPR DOI：`10.1109/CVPR52733.2024.02405`。 |
| `radford2021clip` | 将 `and others` 展开为 PMLR 官方完整作者列表。 |
| `yu2021multiview_tensor_fusion` | 作者姓名由缩写展开为全名。 |
| `cui2024video_anomaly_iqa_attention` | 作者姓名由缩写展开为全名；期刊名展开为 `Alexandria Engineering Journal`。 |
| `yin2024improved_faster_rcnn` | 作者姓名由缩写展开为全名；补充期号 `7`。 |
| `tian2020pde_segmentation_denoising` | 作者姓名由缩写展开为全名；补充期号 `20`。 |
| `qian2020multiview_matrix_correlation` | 作者姓名由缩写展开为全名；补充期号 `5`。 |
| `perez2018film` | 补充 AAAI 页码 `3942--3951`。 |

## 逐条状态

| # | BibTeX key | 状态 |
|---:|---|---|
| 1 | `wang2019edvr` | 已核对；信息正确，仅做会议名/格式规范化。 |
| 2 | `chan2021basicvsr` | 已修正页码和会议条目格式。 |
| 3 | `chan2022basicvsrpp` | 已修正页码和会议条目格式。 |
| 4 | `wan2022rtn` | 已核对；信息正确。 |
| 5 | `lin2024rrtn` | 已核对；保留 `6704--6714` 和现有 DOI。 |
| 6 | `mao2025mambaofr` | 已核对；信息正确，标题大小写略作规范。 |
| 7 | `liang2024vrt` | 已修正作者名。 |
| 8 | `liang2022rvrt` | 已补充 NeurIPS 卷号。 |
| 9 | `gu2024mamba` | 已规范 COLM 条目并补充 OpenReview URL。 |
| 10 | `guo2024mambair` | 已核对；信息正确。 |
| 11 | `lin2017fpn` | 已核对；信息正确。 |
| 12 | `gu2025reidmamba` | 已核对；保留 2026 Early Access 信息，key 不改名。 |
| 13 | `zheng2023diffkendall` | 已修正作者、卷号和页码。 |
| 14 | `kendall1938measure` | 已规范期号并改用 OUP DOI。 |
| 15 | `iizuka2019deepremaster` | 已补充 article number 和 numpages。 |
| 16 | `jantic2019deoldify` | 已改为更标准的 `url` 字段，保留访问日期。 |
| 17 | `li2023shiftnet` | 已修正作者列表。 |
| 18 | `liu2024vmamba` | 已修正作者、卷号和页码。 |
| 19 | `sun2018pcb` | 已核对；信息正确。 |
| 20 | `wang2018mgn` | 已修正作者名。 |
| 21 | `chen2020mocov2` | 已核对；保留 arXiv 元数据。 |
| 22 | `johnson2016perceptual` | 已核对；信息正确。 |
| 23 | `goodfellow2014gan` | 已核对；信息正确，会议名略作规范。 |
| 24 | `zhang2018lpips` | 已核对；信息正确。 |
| 25 | `ding2020dists` | 已修正期号。 |
| 26 | `mittal2012niqe` | 已核对；信息正确；key 中年份未改。 |
| 27 | `mittal2012brisque` | 已核对；信息正确。 |
| 28 | `wang2023clipiqa` | 已核对；信息正确。 |
| 29 | `wang2004ssim` | 已核对；信息正确。 |
| 30 | `nah2019reds` | 已核对；信息正确。 |
| 31 | `kingma2015adam` | 已补充/保留 arXiv 元数据并去除格式问题。 |
| 32 | `gu2022s4` | 已补充 OpenReview URL。 |
| 33 | `tran2025vsrm` | 已修正作者解析形式；删除未能确认的 DOI。 |
| 34 | `lin2024diffbir` | 已核对；信息正确。 |
| 35 | `yu2024supir` | 已补充 DOI。 |
| 36 | `wu2024seesr` | 已补充 DOI。 |
| 37 | `radford2021clip` | 已展开完整作者列表。 |
| 38 | `yu2021multiview_tensor_fusion` | 已展开作者全名。 |
| 39 | `cui2024video_anomaly_iqa_attention` | 已展开作者全名；期刊名规范化。 |
| 40 | `yin2024improved_faster_rcnn` | 已展开作者全名并补充期号。 |
| 41 | `tian2020pde_segmentation_denoising` | 已展开作者全名并补充期号。 |
| 42 | `qian2020multiview_matrix_correlation` | 已展开作者全名并补充期号。 |
| 43 | `perez2018film` | 已补充 AAAI 页码。 |
| 44 | `wang2021hrnet` | 已核对；信息正确。 |
| 45 | `wan2023oldphotopami` | 已核对；信息正确。 |
| 46 | `zamir2022mirnetv2` | 已核对；信息正确；key 中年份未改。 |
| 47 | `kokaram2004missing` | 已核对；信息正确。 |
| 48 | `zhao2017loss_restoration` | 已核对；信息正确。 |
| 49 | `dabov2007bm3d` | 已核对；信息正确。 |
| 50 | `he2013guided` | 已核对；信息正确。 |
