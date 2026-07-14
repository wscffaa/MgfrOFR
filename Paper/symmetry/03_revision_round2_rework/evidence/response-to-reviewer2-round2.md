# Response to Reviewer 2 Comments (Round 2)

Manuscript ID: symmetry-4339980 | Symmetry

Multi-Granularity Feature Decomposition with Ranking-Aware Regularization for Old Film Restoration

## 1. Summary

We thank Reviewer 2 for the careful second-round assessment and for recognizing that the revised manuscript is substantially improved. The remaining comments are minor and focus on evidence clarity, ablation interpretation, qualitative ROI readability, and proofreading. In this second revision, we kept the manuscript structure stable and made targeted changes to: (1) add direct branch-complementarity evidence for RATR; (2) explain the LPIPS/DISTS behavior of the three-branch configuration through the interaction of branch number, token grouping, average fusion, and RATR; (3) rebuild Figures 4 and 5 with clearer enlarged ROI regions; and (4) proofread the affected text and captions.

## 2. Questions for General Evaluation

| Reviewer's Evaluation | Response and Revisions |
| --- | --- |
| Quality of English: English is fine. | We thank the reviewer for this positive assessment. We nevertheless proofread the affected paragraphs and figure captions after the second-round edits. |
| Results presentation: Can be improved. | We added direct branch-similarity evidence from the real 30-clip checkpoint sweep, added pixel-wise error maps, and expanded the ablation and sensitivity discussion. Please see Responses 2 and 3. |
| Figures and tables: Can be improved. | We rebuilt Figures 4 and 5 with a journal-width ROI comparison layout and clearer enlarged local crops. Please see Response 4. |

## 3. Point-by-point response to Comments and Suggestions for Authors

Comments 1: The reviewer noted that the revised manuscript is substantially improved and that the remaining issues are minor.

Response 1:

We appreciate the reviewer's careful reassessment. In this revision, we kept the main manuscript structure stable and made targeted changes only where the second-round report requested clearer evidence, stronger explanation, and improved visual readability.

Revision made:

Kept the revised method, experiment, and discussion structure from the first revision. Rebuilt the final clean manuscript, highlighted-changes manuscript, source package, cover letter, and response file from the same round-2 source tree.

Evidence location:

The updated clean manuscript is provided as `MGFROFR-clean.pdf`, the marked-up manuscript is provided as `MGFROFR-highlighted-changes.pdf`, and the source package is provided as `MGFROFR-latex-source.zip`.

Comments 2: The reviewer suggested adding more direct evidence showing how RATR influences branch complementarity, such as branch-specific activation visualization or feature-similarity analysis during training.

Response 2:

We agree that the RATR claim should be supported by direct branch-level evidence rather than by aggregate restoration scores alone. The revised manuscript now includes a dedicated branch-balance analysis. We analyze pairwise cosine similarity between granularity-branch descriptors and compare the MGFE-only configuration against the full MgfrOFR model. This directly tests whether the branches remain complementary instead of becoming correlated copies of the same evidence.

The revised Figure 9a is regenerated from the real 30-clip branch-similarity sweep rather than from a single representative matrix. At the final 200K checkpoint, RATR reduces the mean off-diagonal branch similarity from 0.863 +/- 0.006 in the MGFE-only configuration to 0.261 +/- 0.143 in the full MgfrOFR model; the final pairwise off-diagonal entries drop from 0.846--0.896 to 0.226--0.310. The same figure also plots the 50K, 100K, 150K, and 200K checkpoint statistics, showing that the separation persists during training. We also include pixel-wise absolute-error maps comparing MambaOFR and MgfrOFR against the ground truth. These maps show that the lower branch correlation corresponds to broader spatial restoration gains, not just isolated local improvements. The discussion further explains the observed specialization pattern: the fine-grained branch responds more strongly to scratches and pixel-level defects, the coarse branch handles broader structural corruption, and the medium branch bridges the two.

Revision made:

Added and clarified the "MGFE--RATR Synergy for Branch Balance" discussion. Added the "Branch Balance Analysis" subsection. Regenerated the branch-similarity figure from the real 30-clip checkpoint sweep, comparing MGFE-only and full MgfrOFR with both final matrices and mean-plus-standard-deviation evolution. Added the pixel-wise absolute-error map figure. Clarified that RATR acts as a diversity regularizer that suppresses redundant temporal-ranking behavior across branches.

Evidence location:

The RATR validation evidence is now described in Section 4.7 under "Branch Balance Analysis." The branch-similarity figure is included as Figure 9a, and the pixel-wise error-map evidence is included as Figure 9b.

Comments 3: The reviewer noted that the ablation discussion should better explain why the three-branch configuration gives a remarkable improvement in LPIPS and DISTS, and whether the gain comes from branch number, token configuration, or their interaction.

Response 3:

We expanded the ablation and sensitivity discussion to separate these factors. The revised ablation table isolates MGFE recalibration and RATR regularization. MGFE-only improves pixel fidelity but trails the full model on LPIPS and DISTS, indicating that recalibration alone does not produce the best fidelity-perception balance. RATR-only improves perceptual balance even before channel-wise feedback is enabled, showing that ranking diversity itself contributes to branch complementarity. The average-fusion full model gives the best combined result across all four full-reference metrics.

We also expanded the granularity and token sensitivity discussion. The one-branch setting gives the best PSNR and SSIM but much worse LPIPS and DISTS, which indicates overfitting to pixel fidelity. The three-branch, 12-token average-fusion setting is not the PSNR maximum, but it is the only setting that combines near-best fidelity with the best LPIPS and DISTS. Therefore, we do not attribute the perceptual improvement to branch count alone. The improvement is explained as the interaction between multi-granularity branches, token grouping, average fusion, and RATR's ranking-diversity constraint.

Revision made:

Expanded the ablation discussion following Table 3. Added a clearer explanation of the MGFE-only, RATR-only, max-fusion, and average-fusion controls. Expanded the sensitivity discussion following the granularity/token table. Clarified that the LPIPS/DISTS gain comes from the interaction of branch decomposition, token configuration, average fusion, and RATR regularization, rather than from simply adding more branches.

Evidence location:

The updated ablation interpretation is in Section 4.4, and the expanded granularity/token sensitivity discussion is in Section 4.5.

Comments 4: The reviewer recommended minor language polishing, slightly larger enlarged ROI regions in Figures 4 and 5, and final proofreading to remove remaining typographical inconsistencies.

Response 4:

We rebuilt both qualitative figures with a journal-width ROI comparison layout. The revised Figure 4 shows full degraded REDS-synthetic input frames in the top row, marks selected local regions with colored boxes, and compares enlarged ROI crops for each restoration method and the ground truth in the following rows. This makes scratches, blotches, local edges, and texture differences more readable.

We also rebuilt Figure 5 for RealFilm-SRWOV real-world clips using the same ROI-based layout. Because no ground truth is available for the real-world clips, the revised Figure 5 compares the degraded input and restoration methods only. The text and caption now explicitly state that the colored boxes mark selected ROI regions and that the enlarged crops compare local restoration details across methods.

Finally, we proofread the affected qualitative-comparison text and captions. We removed the previous column-based Figure 4 description, removed the outdated four-clip real-world list, changed Figure 5 to three representative RealFilm-SRWOV real-world clips, and clarified that the real-world comparison does not include ground-truth references.

Revision made:

Replaced Figure 4 with `figures/Fig4_SOTA_Synthetic_REDS_synthetic_Qualitative.pdf`. Replaced Figure 5 with `figures/Fig5_SOTA_RealWorld_RealFilm_SRWOV_Qualitative.pdf`. Updated the Figure 4 paragraph and caption to describe full-frame inputs plus enlarged ROI crops. Updated the Figure 5 paragraph and caption to describe three RealFilm-SRWOV real-world clips and no ground-truth references. Proofread the revised figure descriptions and removed stale matrix-column and four-clip wording.

Evidence location:

The updated qualitative comparisons are in Section 4.3.3, with the revised Figure 4 and Figure 5 files included in the source package.

## 4. Response to Comments on the Quality of English Language

Point: The reviewer's assessment of the English language was: The English is fine.

We thank the reviewer for this positive assessment. The revised manuscript was nevertheless carefully proofread for terminology consistency, repetition, and sentence length after the second-round figure and discussion updates.

## 5. Additional clarifications

We sincerely thank Reviewer 2 for the constructive second-round evaluation. A clean manuscript, a marked-up manuscript generated from round 1 to round 2, the LaTeX source package, and this response file have been uploaded together for checking.
