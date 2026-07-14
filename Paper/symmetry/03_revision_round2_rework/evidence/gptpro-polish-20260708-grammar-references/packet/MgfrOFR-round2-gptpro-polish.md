# OFR Paper Polish Input Pack

## PROMPT.md

You are editing an MDPI Symmetry revision manuscript for English grammar, clarity, and reference-context consistency.

Task:
Polish the attached manuscript file `01_manuscript_current_full.tex` at sentence level only.

Hard constraints:
1. Return only the complete polished LaTeX content of `01_manuscript_current_full.tex`.
2. Preserve every `%% OFR_SEGMENT_BEGIN ...` and `%% OFR_SEGMENT_END ...` sentinel line exactly.
3. Do not change any scientific content, claims, equations, tables, figures, captions, labels, citations, reference keys, metric values, p-values, dataset sizes, hardware settings, years, or hyperparameters.
4. Do not add, delete, or reorder references. Use `references.bib` and `02_reference_citation_report.md` only to check that citation wording remains relevant to the cited literature.
5. Do not rewrite LaTeX commands or environments. Keep all `\label`, `\ref`, `\eqref`, `\cite`, `\includegraphics`, table markup, formulas, `\textbf`, `\underline`, and math notation intact.
6. Preserve every numeric literal listed in `04_FROZEN_numbers.md` verbatim in count and meaning. If a sentence cannot be improved without touching a frozen number or protected command, leave it unchanged.
7. Do not output a summary, explanation, changelog, markdown table, JSON, patch, or downloadable package.

Editing goals:
- Correct grammar, article usage, tense, agreement, and awkward phrasing.
- Improve readability and academic flow while keeping the current structure.
- Remove repetitive wording when this can be done without changing the technical meaning.
- Make citation-bearing sentences read naturally and ensure the cited reference still supports the sentence.
- Keep the response letter commitments stable: this is a minor proofreading pass after the second revision, not a new scientific revision.

Output format:
Return a single LaTeX code block containing the full polished manuscript content with all OFR segment sentinels preserved. Do not include any text before or after the code block.

## MANIFEST.json

```json
{
  "packet_type": "paper-polish-pack",
  "schema_version": 2,
  "generated_at": "2026-07-08T18:45:40+08:00",
  "scope": "gptpro-polish-grammar-references-round2",
  "project": {
    "root": "/Users/caifeifan/VibeScholar/Antigravity_OFR/projects/001-reidmamba/Paper/symmetry/03_revision_round2_rework",
    "name": "001-reidmamba"
  },
  "artifact": {
    "output_dir": "/Users/caifeifan/VibeScholar/Antigravity_OFR/projects/001-reidmamba/Paper/symmetry/03_revision_round2_rework/evidence/gptpro-polish-20260708-grammar-references/packet"
  },
  "review": {
    "scope_key": "gptpro-polish-grammar-references-round2",
    "round": "round2",
    "mode": "polish"
  },
  "prompt": {
    "path": "PROMPT.md",
    "source": "/Users/caifeifan/VibeScholar/Antigravity_OFR/projects/001-reidmamba/Paper/symmetry/03_revision_round2_rework/evidence/gptpro-polish-20260708-grammar-references/00_GPTPro_prompt.md",
    "sha256": "ead727752d170368f6a910034809ecb789ec898615f2b361400c42b72bed2ce2"
  },
  "limits": {
    "max_file_bytes": 2097152,
    "max_total_bytes": 20971520,
    "allow_binary": false,
    "ack_sensitive_risk": false,
    "budget_check": true
  },
  "files": [
    {
      "path": "files/evidence/gptpro-polish-20260708-grammar-references/01_manuscript_current_full.tex",
      "source_relpath": "evidence/gptpro-polish-20260708-grammar-references/01_manuscript_current_full.tex",
      "bytes": 81102,
      "sha256": "622bef146b05399110de8f7721a13f19760ecb4154eab89db1023b0d0303472a",
      "binary": false
    },
    {
      "path": "files/evidence/gptpro-polish-20260708-grammar-references/04_FROZEN_numbers.md",
      "source_relpath": "evidence/gptpro-polish-20260708-grammar-references/04_FROZEN_numbers.md",
      "bytes": 21327,
      "sha256": "a650c9935a97d685b2601436f41991c153564e5b37b522c67539ac6e3b76f0db",
      "binary": false
    },
    {
      "path": "files/evidence/gptpro-polish-20260708-grammar-references/02_reference_citation_report.md",
      "source_relpath": "evidence/gptpro-polish-20260708-grammar-references/02_reference_citation_report.md",
      "bytes": 8048,
      "sha256": "eff3a1e18fa612c2a5c81c0f89c7422d636b5cd950bd76537415f77ba37a93cc",
      "binary": false
    },
    {
      "path": "files/source/references.bib",
      "source_relpath": "source/references.bib",
      "bytes": 20348,
      "sha256": "0bd46b8da0a04287edb4aba0b6ab5b73e6fdefee28398d6f30133788a504e74a",
      "binary": false
    }
  ],
  "sensitive_findings": []
}
```

## Files

### `evidence/gptpro-polish-20260708-grammar-references/01_manuscript_current_full.tex`

```text
%% OFR_SEGMENT_BEGIN abstract b74b80130941cd4bcc12a2772c75326cccc8543dca82b332f21965a86378903e
\abstract{Old film restoration remains challenging because archival footage often contains scratches, blotches, flicker, blur, and temporal artifacts that disturb the balance between structural recovery, regional texture repair, and fine artifact suppression. To address this problem, we propose MgfrOFR, a multi-granularity extension of a Mamba-based old film restoration backbone. First, MgfrOFR decomposes propagated features into coarse-to-fine restoration branches and feeds branch summaries back through channel-wise recalibration, allowing different degradation scales to be represented without competing in a single feature stream. Second, it introduces a ranking-aware triplet regularizer that penalizes correlated temporal-similarity rankings across branches during training while preserving the baseline inference interface. Experiments on the SRWOV benchmark show statistically significant fidelity gains on synthetic clips, strong no-reference naturalness on real-world archival footage, and a bounded perceptual-quality trade-off. These results indicate that representation-level branch balance provides an effective inductive bias for old film restoration under heterogeneous and asymmetric degradation.}
%% OFR_SEGMENT_END abstract
%% OFR_SEGMENT_BEGIN introduction db34ac3a0dde65c8988cb45d7cee087bfd3955d03562b85f56ea485d50400be9
\section{Introduction}
\label{sec:introduction}

Old films carry cinematic heritage, historical documentaries, and large archival collections, yet the film stock that stores them keeps decaying. Digital restoration offers a practical route to revitalize such material~\cite{iizuka2019deepremaster}. The real difficulty is that aged footage is rarely damaged in a single way. Scratches, dust, blotches, flicker, blur, grain, and fading accumulate within the same clip, and they act on very different spatial scales, from large structural collapse down to thin local artifacts. This scale span sets old film restoration apart from ordinary video enhancement. A successful restoration must hold coarse structural recovery, regional texture repair, and fine artifact suppression in balance---a representation-level symmetry that the asymmetric, heterogeneous degradation constantly works against.

Learning-based old film restoration has advanced through end-to-end video restoration frameworks. RTN pioneered bidirectional recurrent propagation with a learnable defect mask, but its restoration evidence still flows through a single recurrent stream~\cite{wan2022rtn}. RRTN added recursive transformer propagation for stronger temporal alignment; structural recovery and fine artifact suppression remain jointly encoded~\cite{lin2024rrtn}. MambaOFR then brought state space models into old film restoration, improving efficiency and establishing the Synthetic/Real-World Old Video (SRWOV) benchmark~\cite{mao2025mambaofr,gu2024mamba,guo2024mambair}. Even so, it routes every degradation scale through one propagated feature pathway. These methods share a single weakness: when heterogeneous signals compete in one latent space, coarse recovery overwrites fine evidence, and local artifact suppression distorts global structure.

This symmetry works at the representation level rather than as an object-level shape constraint. A symmetric representation keeps restoration evidence balanced across granularity-specific branches while maintaining a consistent temporal correspondence structure across frames. Because our branch-diversity objective is invariant under permutations of the granularity branches (the symmetric group $\mathcal{S}_G$), this balance is a permutation symmetry in the machine-learning sense---a standard group-symmetry principle---rather than a visible geometric one, which places MgfrOFR within symmetry-driven representation learning for image restoration. This view fits old film restoration because its degradation space is hierarchical. Missing regions and large blotches need global context, grain and flicker need regional modeling, and fine scratches or dust need local precision. Existing multi-granularity designs target detection or recognition~\cite{lin2017fpn,wang2021hrnet,sun2018pcb,wang2018mgn,gu2025reidmamba}. Naive multi-branch extensions can collapse into correlated features unless branch diversity is explicitly enforced. This gap motivates explicit granularity-separated restoration branches.

We propose MgfrOFR, which augments MambaOFR with two complementary components (Figure~\ref{fig:architecture}). The Multi-Granularity Feature Extractor (MGFE) reorganizes propagated Mamba features into coarse-to-fine restoration branches, so that structural completion, regional repair, and fine-detail suppression are carried by dedicated descriptors instead of competing in one hidden stream. It also feeds branch summaries back into the spatial stream through channel-wise recalibration. The Ranking-Aware Triplet Regularization (RATR) keeps these branches from collapsing into redundant representations by penalizing correlated rankings on temporal correspondences. RATR defines branch diversity over temporal correspondences rather than identity labels, which fits the restoration setting.

Under a unified reproduction protocol on SRWOV, MgfrOFR preserves the efficient Mamba backbone of MambaOFR and adds explicit granularity control at modest overhead. The main contributions of this work are summarized as follows:
\begin{enumerate}
    \item We formulate old film restoration as representation-level symmetry under heterogeneous degradation, treating coarse structural recovery, regional texture repair, and fine artifact suppression as complementary feature components that stay balanced despite spatial and temporal asymmetry.
    \item We design MGFE, a multi-granularity feature decomposition for Mamba-based old film restoration that inserts learnable restoration tokens into propagated features, aggregates them into coarse-to-fine branches, and feeds branch summaries back to the spatial stream through channel-wise recalibration.
    \item We introduce RATR, a ranking-aware triplet regularizer that penalizes correlated temporal-similarity rankings across granularity branches with differentiable rank correlation, improving branch complementarity and reducing redundancy while preserving the original baseline inference interface.
    \item We conduct a unified evaluation on the SRWOV benchmark covering synthetic and real-world archival footage, where statistical tests, ablation studies, and complexity analysis show that MgfrOFR improves restoration fidelity and naturalness at modest additional computational cost.
\end{enumerate}
%% OFR_SEGMENT_END introduction
%% OFR_SEGMENT_BEGIN related_work f72fe8ad693edbc2d2806dc74a409ec8ff727b474a1ff5031296ade40b722ee1
\section{Related Work}
\label{sec:related}

\subsection{Old Film and Video Restoration}
\label{subsec:ofr}

Old film restoration differs from general video restoration in that it must jointly address structured artifacts (scratches, dust, blotches), photometric degradation (flicker, grain, fading), and quality degeneration (blur, noise). Traditional approaches decompose the problem into detection and inpainting stages, relying on hand-crafted features and interpolation-based filling~\cite{kokaram2004missing} or sparse collaborative filtering~\cite{dabov2007bm3d,he2013guided}. While computationally efficient, these methods lack semantic understanding of video content and leave photometric degradations unaddressed. Deep learning shifted old film restoration toward end-to-end frameworks: DeepRemaster~\cite{iizuka2019deepremaster} processes spatiotemporal volumes with 3D convolutions, RTN~\cite{wan2022rtn} introduces bidirectional recurrent propagation with a learnable soft defect mask, and RRTN~\cite{lin2024rrtn} strengthens alignment via recursive transformer networks with second-order grid propagation. MambaOFR~\cite{mao2025mambaofr} replaces computationally expensive blocks with MambaIR-style~\cite{guo2024mambair} state-space modules and establishes the SRWOV benchmark for dedicated old film restoration evaluation.

General video restoration methods such as EDVR~\cite{wang2019edvr}, BasicVSR~\cite{chan2021basicvsr}, BasicVSR++~\cite{chan2022basicvsrpp}, VRT~\cite{liang2024vrt}, and RVRT~\cite{liang2022rvrt} provide strong temporal modeling, but they do not incorporate defect handling specific to old film restoration. Recent diffusion and foundation-prior restoration systems, including DiffBIR~\cite{lin2024diffbir}, SUPIR~\cite{yu2024supir}, and SeeSR~\cite{wu2024seesr}, improve perceptual detail for blind image restoration or real-world super-resolution, but they are not designed around temporal old-film defects or SRWOV-style video restoration protocols. Despite this progress, existing old film restoration methods still encode structural completion, regional repair, and fine-detail suppression through a single propagated latent space. This motivates our multi-granularity decomposition approach.

\subsection{State Space Models for Vision}
\label{subsec:ssm}

The computational cost of self-attention scales quadratically with sequence length, posing a practical barrier for high-resolution video processing. Structured state space sequence models~\cite{gu2022s4} reformulate sequence modeling through continuous-time state transitions, reducing complexity from $O(L^2)$ to $O(L)$ while maintaining a global receptive field. Mamba~\cite{gu2024mamba} further introduces selective state transitions with hardware-aware recurrence, enabling content-dependent filtering. The adaptation of SSMs to visual domains has produced strong baselines: MambaIR~\cite{guo2024mambair} demonstrates 2D selective scanning for image restoration, VMamba~\cite{liu2024vmamba} builds hierarchical feature pyramids with four scanning routes, and VSRM~\cite{tran2025vsrm} alternates spatial and temporal Mamba blocks for video super-resolution at linear cost.

These properties are well-suited for old film restoration, which couples long temporal dependency, large spatial damage, and high-resolution input. MambaOFR~\cite{mao2025mambaofr} validates that Mamba-based propagation outperforms transformer counterparts on both efficiency and quality. However, linear-cost long-range aggregation alone does not decide what restoration evidence each feature position retains; the backbone treats all degradation scales uniformly. Our work augments the SSM feature flow with explicit multi-granularity descriptors rather than replacing the backbone.

\subsection{Multi-Scale and Multi-Branch Representations}
\label{subsec:multigran}

A single feature scale often cannot encode both global structure and fine-grained local evidence simultaneously. Feature Pyramid Networks~\cite{lin2017fpn} and HRNet~\cite{wang2021hrnet} establish that explicit multi-scale decomposition improves dense prediction, while MIRNet-v2~\cite{zamir2022mirnetv2} shows that complementary multi-scale context enhances low-level reconstruction quality. In person re-identification, PCB~\cite{sun2018pcb} decomposes features along spatial stripes, MGN~\cite{wang2018mgn} combines global and local branches at different partition granularities, and ReIDMamba~\cite{gu2025reidmamba} adapts this paradigm to state space models. These methods show that branch structure can expose complementary evidence, but their supervision and feature semantics target recognition rather than restoration.

\subsection{Diversity and Ranking Regularization}
\label{subsec:diversity_ranking}

The consistent lesson across these works is that extra branches provide benefit only when they capture complementary cues rather than correlated copies of the same evidence. Contrastive learning~\cite{chen2020mocov2} provides a general diversity mechanism, but it does not directly regulate pairwise ordering behavior across branches: two branches can produce different feature magnitudes yet rank all candidates identically, yielding diversity in norm but redundancy in discriminative structure. Differentiable Kendall's Tau~\cite{zheng2023diffkendall} enables gradient-based penalization of correlated rankings, a property that naturally applies to flow-guided temporal correspondences in old film restoration.

\subsection{Representation Symmetry in Restoration}
\label{subsec:symmetry_ai}

In AI-based image processing, symmetry can be interpreted beyond visible object geometry. A learned representation may be symmetric when complementary evidence sources remain balanced, comparable, and consistently organized across samples; asymmetry appears when optimization favors one dominant cue. Feature-fusion and correlation-based representation studies show that multi-view or multi-branch features need explicit organization rather than simple concatenation~\cite{yu2021multiview_tensor_fusion,qian2020multiview_matrix_correlation}, and feature-wise modulation provides a practical way to inject conditioning signals into image-processing networks~\cite{perez2018film}. For old film restoration, this view is useful because film damage is inherently asymmetric across regions and frames. In MgfrOFR this representation symmetry is made precise as two group invariances of the training objective---branch-permutation invariance under the symmetric group $\mathcal{S}_G$ and direction-exchange invariance under the bidirectional $\mathbb{Z}_2$ action (Section~\ref{subsec:symmetry_property}).

Our design is inspired by this line of work, but the restoration setting changes the formulation in three important ways. First, the branch tokens are inserted into propagated restoration features rather than identity-oriented recognition embeddings. Second, the branch summaries are fed back into the restoration stream through channel-wise recalibration, so they affect reconstruction rather than only auxiliary supervision. Third, positives and negatives are defined by temporal correspondence within and across clips rather than person identities. The analysis above highlights two gaps in old film restoration: the absence of explicit multi-granularity feature decomposition within the temporal propagation pipeline, and the lack of diversity regularization to ensure that parallel feature branches capture complementary restoration evidence. Unlike multi-scale pyramids, token/stripe recognition models, and generic diversity losses, MgfrOFR is the only design considered here whose branch structure carries an explicit permutation-and-exchange symmetry rather than acting on feature magnitude alone. MgfrOFR addresses both gaps within a unified framework, as detailed in Section~\ref{sec:method}.
%% OFR_SEGMENT_END related_work
%% OFR_SEGMENT_BEGIN method f06d4df19dcacfffef9ad0708604becd523aff4af1ccdb5312c15095ac51662f
\section{Methods}
\label{sec:method}

\subsection{Problem Setup}
\label{subsec:problem_setup}

Given a degraded old-film clip $X=\{x_t\}_{t=1}^{T}$, we aim to recover a clean clip $Y=\{y_t\}_{t=1}^{T}$ in which image content is restored and structured film defects and photometric degradation are removed. Synthetic SRWOV clips come with paired clean frames and give direct supervision. Real-world archival clips have no ground truth, so we evaluate them with no-reference quality metrics and qualitative inspection. Old-film degradations vary in both spatial scale and time, and a restoration model must remove them without breaking temporal consistency.

\subsection{Input Representation}
\label{subsec:input_representation}

Each input frame is an RGB image, and the baseline propagation module turns the clip into backward and forward feature streams. At every time step $t$, motion-aware propagation yields aligned feature maps $f_t^{b}, f_t^{f} \in \mathbb{R}^{C_f \times H \times W}$. MgfrOFR operates entirely on these propagated maps: MGFE takes each map, returns a recalibrated map of the same spatial size and channel count, and produces the branch descriptors that RATR uses during training.

MgfrOFR keeps the bidirectional propagation framework of MambaOFR~\cite{mao2025mambaofr} but replaces its single-granularity restoration view with an explicit coarse-to-fine pipeline. Given the degraded clip $X=\{x_t\}_{t=1}^{T}$, the baseline first propagates content backward and forward so that neighboring frames are motion-aligned before restoration, and MgfrOFR builds on these aligned features. Old-film damage is spatially and temporally asymmetric: a scratch may cover one region in one frame and vanish in the next, yet restoration should still weigh coarse, medium, and fine evidence in a balanced way. This cross-granularity balance is the feature-space symmetry our design pursues.

MGFE turns each propagated feature map into a token sequence, inserts learnable restoration tokens, and reads branch descriptors from progressively fused token groups; their summaries flow back to the propagated feature through channel-wise recalibration. RATR acts only during training, where it discourages the branches from ranking samples in the same redundant way, and it is switched off at inference. The reconstruction head is inherited unchanged from MambaOFR and outputs the restored frame. Figure~\ref{fig:architecture} shows how these components fit together.

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{figures/Fig1_mgfrofr_architecture.pdf}
\caption{The MgfrOFR framework illustrates how MGFE decomposes propagated features into $G{=}3$ multi-granularity restoration-token branches for channel-wise recalibration. RATR is used only during training (dashed red path) to penalize redundant temporal-ranking correlations and produce $\mathcal{L}_{\text{intra}}$ and $\mathcal{L}_{\text{inter}}$.\label{fig:architecture}}
\end{figure}

\subsection{Pipeline Overview}
\label{subsec:overview}

At time step $t$, the baseline provides the propagated maps $f_t^{b}, f_t^{f} \in \mathbb{R}^{C_f \times H \times W}$, and MGFE maps each one into a recalibrated feature map together with a set of branch descriptors:

\begin{equation}
\left(\widetilde{f}_t^{d}, B_t^{d}\right)=\operatorname{MGFE}\!\left(f_t^{d}\right), \quad d \in \{b,f\},
\end{equation}

where $d$ indexes the propagation direction, $B_t^{d} \in \mathbb{R}^{G \times D}$ is the branch-descriptor tensor and $D=C_f$ in this work. The reconstruction head keeps the original MambaOFR interface and combines the two recalibrated directional features:

\begin{equation}
y_t = \mathcal{R}\!\left([\widetilde{f}_t^{b};\widetilde{f}_t^{f}], x_t\right),
\qquad
B_t = \frac{1}{2}\left(B_t^{b}+B_t^{f}\right),
\label{eq:mgfrofr_overview_2}
\end{equation}

where $\mathcal{R}(\cdot)$ is the unchanged reconstruction head of MambaOFR and $[\cdot;\cdot]$ denotes channel concatenation. Averaging the two directional descriptors before RATR, as in Equation~\eqref{eq:mgfrofr_overview_2}, lets the diversity regularizer act on a single descriptor tensor per frame rather than on two nearly identical streams. Figure~\ref{fig:architecture} traces this data flow, and Algorithm~\ref{alg:mgfrofr} summarizes the forward pass.

\begin{algorithm}[H]
\caption{MgfrOFR forward pass for a clip of length $T$.\label{alg:mgfrofr}}
\begin{algorithmic}[1]
\Require Degraded clip $X=\{x_t\}_{t=1}^{T}$
\Ensure Restored frames $\{y_t\}_{t=1}^{T}$
\State Initialize descriptor buffer $\mathcal{B} \leftarrow \emptyset$
\For{$t = 1$ to $T$}
    \State $f_t^{b}, f_t^{f} \leftarrow \text{Backbone}(X, t)$ \Comment{Bidirectional propagation}
    \For{$d \in \{b, f\}$}
        \State $\widetilde{f}_t^{d}, B_t^{d} \leftarrow \text{MGFE}(f_t^{d})$ \Comment{Multi-granularity decomposition}
    \EndFor
    \State $B_t \leftarrow \frac{1}{2}(B_t^{b} + B_t^{f})$ \Comment{Average branch descriptors}
    \State $\mathcal{B} \leftarrow \mathcal{B} \cup \{B_t\}$ \Comment{Accumulate into batch buffer}
    \State $y_t \leftarrow \mathcal{R}([\widetilde{f}_t^{b}; \widetilde{f}_t^{f}], x_t)$ \Comment{Reconstruction}
\EndFor
\If{training}
    \State $\mathcal{L}_{\text{ratr}} \leftarrow \text{RATR}(\{B_t\}_{t=1}^{T})$ \Comment{Applied on full batch after accumulation}
    \State $\mathcal{L}_{\text{total}} \leftarrow \mathcal{L}_{\text{pix}} + \lambda_{\text{perc}}\mathcal{L}_{\text{perc}} + \lambda_{\text{gan}}\mathcal{L}_{\text{gan}} + \lambda_{\text{ratr}}\mathcal{L}_{\text{ratr}}$
\EndIf
\end{algorithmic}
\end{algorithm}

\subsection{Baseline Interface and Preserved Components}
\label{subsec:baseline_interface}

MgfrOFR leaves the MambaOFR backbone, propagation order, reconstruction head, and training loop untouched. At inference the only addition is MGFE, which maps $f_t^{d}$ to $\widetilde{f}_t^{d}$ without changing the tensor shape; RATR is an auxiliary loss on the branch descriptors and plays no role once training ends. The reconstruction head therefore behaves exactly as in the baseline, still taking the concatenated backward and forward features together with the current degraded frame.

\subsection{Multi-Granularity Feature Extractor (MGFE)}
\label{subsec:mgfe}

Old films are damaged at very different scales: large missing regions, mid-scale blotches, and thin scratches each need a different aggregation range. A single restoration feature has to serve all of them at once, so fine detail and coarse structure compete inside the same channels. MGFE resolves this by keeping the propagated feature as a shared spatial carrier and, alongside it, exposing several restoration-token branches that aggregate at different rates; the branch summaries are fed back to the carrier as a recalibration signal. Each damage scale then gets a dedicated branch, while reconstruction still reads from one common feature. Figure~\ref{fig:mgfe_detail} details the design.

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{figures/Fig2_mgfe_module_detail.pdf}
\caption{MGFE illustrates the decomposition of propagated features into $G{=}3$ restoration-token branches. $M{=}12$ learnable restoration tokens are inserted into image tokens, fused by progressive average fusion, and summarized into descriptors that generate scale/shift parameters for channel-wise recalibration.\label{fig:mgfe_detail}}
\end{figure}

Since MGFE processes each propagation direction identically, we drop the direction superscript $d$ and write $f_t \in \mathbb{R}^{C_f \times H \times W}$ for brevity. We first flatten it into an image-token sequence

\begin{equation}
Z_t = \operatorname{Flat}(f_t) \in \mathbb{R}^{N \times C_f},
\qquad
N = H W,
\end{equation}

where $\operatorname{Flat}(\cdot)$ preserves raster order and stacks spatial positions into token form. We then append $M$ learnable restoration tokens $R \in \mathbb{R}^{M \times C_f}$ and insert them into the image-token stream through an operator $\Pi(\cdot,\cdot)$. The restoration-token matrix is initialized from a truncated normal distribution with standard deviation 0.02 and optimized jointly with the restoration network:

\begin{equation}
\widehat{Z}_t = \Pi(Z_t, R) \in \mathbb{R}^{(N+M)\times C_f}.
\end{equation}

The insertion $\Pi$ partitions the $N$ image tokens into $M{+}1$ approximately equal chunks and places one restoration token after each of the first $M$ chunks, keeping the original image-token order. Each chunk receives $\lfloor N/(M{+}1)\rfloor$ or $\lceil N/(M{+}1)\rceil$ image tokens, so the total stays exactly $N$. For example, with $M=3$ and $N=9$ the four chunks hold $\{3,2,2,2\}$ image tokens and the three restoration tokens land at cumulative positions $\{3,6,9\}$ in the 12-token interleaved sequence. Spacing the tokens uniformly this way gives them balanced receptive ranges over the full spatial support.

MGFE then builds $G$ granularity branches by progressively fusing restoration tokens, following the progressive fusion scheme introduced in ReIDMamba~\cite{gu2025reidmamba} and adapted here for spatial restoration features. To make every branch well-defined, the number of restoration tokens must satisfy the divisibility constraint
\begin{equation}
M = k \cdot 2^{G-1},\quad k \in \mathbb{N}^{+},
\end{equation}
so that every branch size $M_g = M/2^g$ is an integer for $g\in\{0,\ldots,G-1\}$. We use $G=3$ and $M=12$ ($k=3$) throughout; see Section~\ref{subsec:sensitivity} for alternative configurations.

For branch $g \in \{0,\ldots,G-1\}$, MGFE fuses restoration tokens with a sampling rate of $2^g$. The fused restoration tokens are defined as

\begin{equation}
R^{(g)}[j] =
\mathcal{F}\!\left(
\left\{R[j{\cdot}2^g+k]\right\}_{k=0}^{2^g-1}
\right),\quad
j = 0,\ldots,M_g-1,
\end{equation}

where $\mathcal{F}(\cdot)$ denotes an element-wise average over all tokens in the fusion group:

\begin{equation}
\mathcal{F}\!\left(
\left\{R[j\cdot2^g+k]\right\}_{k=0}^{2^g-1}
\right)
= \frac{1}{2^g}\sum_{k=0}^{2^g-1} R[j\cdot2^g+k]\;\in\mathbb{R}^{C_f}.
\label{eq:avg_fusion}
\end{equation}

The average is taken channel-wise. We use average fusion in the main MgfrOFR configuration because it keeps all restoration tokens contributing to the branch descriptor and avoids a single high-response token dominating the recalibration signal. The max-fusion variant is retained as a control in Section~\ref{subsec:ablation}; its lower full-reference scores motivate average fusion as the default. A smaller $g$ keeps more tokens and preserves fine local detail; a larger $g$ pools a wider support and emphasizes coarse context.

The fused tokens are re-inserted into the same image-token sequence using the same uniform-spacing insertion rule:

\begin{equation}
\widehat{Z}_t^{(g)} = \Pi\!\left(Z_t,R^{(g)}\right),
\end{equation}

and the resulting sequence is processed by a lightweight branch-specific token mixer $\Phi_g(\cdot)$:

\begin{equation}
U_t^{(g)} = \Phi_g\!\left(\widehat{Z}_t^{(g)}\right)
\in \mathbb{R}^{(N+M_g)\times C_f},
\end{equation}

where $M_g = M/2^g$. Each $\Phi_g$ consists of two sequential linear-complexity token blocks, each containing a context-augmented projection sublayer and a feed-forward sublayer. The projection sublayer first applies LayerNorm, then computes a global context vector via mean pooling over the token dimension and adds it (through a learned linear projection) to the per-token linear projection, followed by a residual connection. The feed-forward sublayer applies LayerNorm followed by a two-layer MLP with GELU activation and hidden dimension $2C_f$, again with a residual connection. Formally, for input tokens $\mathbf{h}$, each block computes
\begin{equation}
\mathbf{h}' = \mathbf{h} + W_t\,\mathrm{LN}(\mathbf{h}) + W_c\,\overline{\mathrm{LN}(\mathbf{h})},\qquad
\mathbf{h}'' = \mathbf{h}' + \mathrm{MLP}(\mathrm{LN}(\mathbf{h}')),
\end{equation}
where $\overline{(\cdot)}$ denotes mean pooling over the token dimension, $W_t,W_c\in\mathbb{R}^{C_f\times C_f}$ are learned projections, and MLP consists of $\mathrm{Linear}(C_f\!\rightarrow\!2C_f)\!\rightarrow\!\mathrm{GELU}\!\rightarrow\!\mathrm{Linear}(2C_f\!\rightarrow\!C_f)$. The global context term $W_c\,\overline{\mathrm{LN}(\mathbf{h})}$ gives every token a cheap summary of the whole sequence, so tokens exchange information at linear cost. Each branch owns its pair of token blocks and can specialize to its granularity, and because the blocks are small the extra parameters stay modest.

After branch processing, we summarize each branch by averaging the updated restoration-token positions:

\begin{equation}
b_t^{(g)} =
\frac{1}{M_g}
\sum_{m=1}^{M_g}
U_t^{(g)}[\pi_m^{(M_g)}]
\in \mathbb{R}^{D},
\end{equation}

where $\{\pi_m^{(M_g)}\}_{m=1}^{M_g}$ denote the uniformly spaced insertion positions for $M_g$ tokens, and $D=C_f$. Stacking all branch descriptors gives

\begin{equation}
B_t =
\left[
b_t^{(0)}, b_t^{(1)}, \ldots, b_t^{(G-1)}
\right]^\top
\in \mathbb{R}^{G \times D}.
\end{equation}

Because all descriptors come from the same propagated feature but at different fusion rates, they stay semantically aligned while differing in granularity. RATR later operates on this descriptor tensor $B_t$.

MGFE further converts the branch descriptors into a channel-wise recalibration signal. We first average the branch context,

\begin{equation}
c_t = \frac{1}{G}\sum_{g=0}^{G-1}b_t^{(g)},
\qquad
[\boldsymbol{\gamma}_t,\boldsymbol{\beta}_t] = \Psi(c_t),
\label{eq:recalibration_context}
\end{equation}

where $\Psi(\cdot)$ is a projection head consisting of $\mathrm{LayerNorm}\!\rightarrow\!\mathrm{Linear}(C_f\!\rightarrow\!2C_f)\!\rightarrow\!\mathrm{GELU}\!\rightarrow\!\mathrm{Linear}(2C_f\!\rightarrow\!2C_f)$ that outputs concatenated scale and shift vectors. The recalibrated propagated feature is then

\begin{equation}
\widetilde{f}_t =
f_t \odot
\left(1+\tanh(\boldsymbol{\gamma}_t)\right)
+ 0.1\,\tanh(\boldsymbol{\beta}_t),
\label{eq:recalibration}
\end{equation}

where the vectors from Equation~\eqref{eq:recalibration_context} are broadcast over the spatial dimensions. The multiplicative term $(1+\tanh(\boldsymbol{\gamma}_t))$ starts near unity, and the small additive coefficient $0.1$ caps the shift at about $10\%$ of the $\tanh$ range, following the conservative residual scaling of FiLM-style modulation~\cite{perez2018film}. The recalibrated feature therefore stays close to the propagated feature while the branch context is still uninformative, and the model reproduces baseline behavior early in training. As the descriptors sharpen, the coarse branches push global structure and the fine branches highlight local damage.

MGFE produces two outputs from the same propagated feature: the branch descriptors $B_t$ and the recalibration signal $(\boldsymbol{\gamma}_t, \boldsymbol{\beta}_t)$. The descriptors feed the ranking regularizer of Section~\ref{subsec:ratr}, while the recalibration modulates the propagated feature by granularity. Keeping them separate lets us switch off recalibration without touching the descriptors, as in the RATR-only configuration of Section~\ref{subsec:ablation}. Explicit branches, however, do not guarantee complementary features. When every branch ranks samples in the same order, they collapse into redundant descriptors, exactly what the next regularizer prevents.

\subsection{Ranking-Aware Triplet Regularization (RATR)}
\label{subsec:ratr}

RATR keeps the branches from collapsing by penalizing how strongly their rankings agree. Making the descriptors orthogonal is not enough: two branches can be orthogonal yet still order the same samples identically, which leaves them redundant and undoes the balance MGFE builds. What matters is the ordering. For an anchor frame compared against nearby positives and harder negatives, RATR measures whether two branches rank that candidate set alike, using Kendall's~\cite{kendall1938measure} rank correlation coefficient made differentiable by DiffKendall~\cite{zheng2023diffkendall}. Figure~\ref{fig:ratr_detail} shows the workflow.

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{figures/Fig3_ratr_module_detail.pdf}
\caption{RATR illustrates how differentiable Kendall's Tau compares branch-specific ranking sequences from temporal correspondences. Neighbor frames define positives, distant same-video frames and cross-video centroids define negatives, producing $\mathcal{L}_{\text{intra}}$ and $\mathcal{L}_{\text{inter}}$ during training only.\label{fig:ratr_detail}}
\end{figure}

Let the averaged branch descriptors from Equation~\eqref{eq:mgfrofr_overview_2} be organized as a 4D tensor of shape $N_b\times T\times G\times D$, where $N_b$ is the batch size. We flatten batch and time into $\bar{N}=N_b T$ samples and normalize the descriptors branch-wise:

\begin{equation}
\widehat{b}_i^{(g)} =
\frac{b_i^{(g)}}{\|b_i^{(g)}\|_2},
\qquad
i=1,\ldots,\bar{N}.
\end{equation}

For each branch $g$, we compute a cosine-similarity matrix

\begin{equation}
\mathcal{S}^{(g)}[i,j] =
\left\langle
\widehat{b}_i^{(g)},
\widehat{b}_j^{(g)}
\right\rangle.
\end{equation}

This matrix is the source of the rankings rather than a supervision target itself: each anchor draws one positive ranking sequence and one negative ranking sequence from it, forming the anchor-positive-negative triplet that RATR regularizes.

For anchor $i$, the positive set is defined from temporal correspondences within the same clip:

\begin{equation}
\mathcal{P}(i)=
\bigl\{
j \mid v_j=v_i,\;
|t_j-t_i|=1
\bigr\},
\end{equation}

where $v_i$ and $t_i$ are the clip and frame indices of sample $i$. Adjacent frames are a natural choice here: the flow-guided deformable alignment in MambaOFR has already warped neighboring frames onto the anchor before MGFE runs, so after alignment they are the most reliable feature-domain proxy for true correspondences. Since $|\mathcal{P}(i)| \le 2$ (at most one predecessor and one successor), boundary frames have only a single positive neighbor, and we compute the intra-ranking term only on anchors that have at least two positives:
\begin{equation}
\mathcal{I}_{\text{intra}}=
\bigl\{
i \mid |\mathcal{P}(i)| \ge 2
\bigr\}.
\end{equation}
For the seven-frame clips used in training, this drops only the first and last frame of each clip, and every interior anchor contributes one pairwise ordering comparison to $\mathcal{L}_{\text{intra}}$. This is enough in practice: $\mathcal{L}_{\text{intra}}$ is averaged over many valid anchors per batch, and $\mathcal{L}_{\text{inter}}$ adds a complementary signal from the richer negative set.

Negative evidence is drawn from two harder sources: temporally distant frames inside the same clip and clip-level representatives from other clips. The same-video negatives are

\begin{equation}
\mathcal{N}_{sv}(i)=
\bigl\{
j \mid v_j=v_i,\;
|t_j-t_i|>1
\bigr\},
\end{equation}

and the clip-level centroid for another video $v\neq v_i$ is

\begin{equation}
\bar{b}_{v}^{(g)} =
\frac{1}{|\mathcal{T}_v|}
\sum_{t\in\mathcal{T}_v}
\widehat{b}_{(v,t)}^{(g)},
\end{equation}

where $\mathcal{T}_v$ denotes the set of frame indices in clip $v$. We then construct the negative ranking sequence as

\begin{equation}
\bar{\mathcal{S}}_i^{(g)} =
\Bigl[\mathcal{S}^{(g)}[i,j]\Bigr]_{j\in\mathcal{N}_{sv}(i)}
\oplus
\Bigl[\bigl\langle \widehat{b}_i^{(g)},\,\bar{b}_v^{(g)} \bigr\rangle\Bigr]_{v\neq v_i},
\end{equation}

where $\oplus$ denotes sequence concatenation. Distant frames from the same clip are hard negatives: they share content and degradation with the anchor but are no longer immediate neighbors. Using one centroid per other clip gives a stable clip-level negative and keeps the cost linear instead of the $O(\bar{N}^2)$ of comparing every cross-clip frame pair.

To compare how two branches rank the same candidate set, we adopt a differentiable version of Kendall's Tau. For sequences $p,q\in\mathbb{R}^{L}$, the differentiable statistic is

\begin{equation}
\mathrm{DKTau}(p,q;\tau)
= \frac{1}{\binom{L}{2}}
\sum_{1\le u < v \le L}
\tanh\!\!\left(\frac{p_u-p_v}{\tau}\right)
\cdot
\tanh\!\!\left(\frac{q_u-q_v}{\tau}\right),
\label{eq:dktau}
\end{equation}

where $\tau>0$ is a temperature parameter. As $\tau\rightarrow 0$, Equation~\eqref{eq:dktau} approaches the hard sign comparison used in the exact Kendall coefficient; as $\tau$ becomes too large, pairwise order differences are oversmoothed and gradients vanish. We set $\tau=0.1$ (see Section~\ref{subsec:sensitivity} for the sensitivity to this choice). A lower value of $\mathrm{DKTau}(p,q;\tau)$ indicates weaker ranking correlation between branches and therefore stronger branch complementarity.

Using Equation~\eqref{eq:dktau}, we compute the positive-ranking correlation loss as

\begin{equation}
\mathcal{L}_{\text{intra}} =
\frac{1}{|\mathcal{I}_{\text{intra}}| \binom{G}{2}}
\sum_{i\in\mathcal{I}_{\text{intra}}}
\sum_{g < g'}
\mathrm{DKTau}\!\Bigl(
\mathcal{S}^{(g)}[i,\mathcal{P}(i)],\,
\mathcal{S}^{(g')}[i,\mathcal{P}(i)];\,\tau
\Bigr),
\label{eq:loss_intra}
\end{equation}

and the negative-ranking correlation loss as

\begin{equation}
\mathcal{L}_{\text{inter}} =
\frac{1}{\bar{N} \binom{G}{2}}
\sum_{i=1}^{\bar{N}}
\sum_{g < g'}
\mathrm{DKTau}\!\Bigl(
\bar{\mathcal{S}}_i^{(g)},\,
\bar{\mathcal{S}}_i^{(g')};\,
\tau
\Bigr).
\end{equation}

The final ranking-aware regularizer is

\begin{equation}
\mathcal{L}_{\text{ratr}} =
\lambda_{\text{intra}}\,\mathcal{L}_{\text{intra}}
+ \lambda_{\text{inter}}\,\mathcal{L}_{\text{inter}}.
\label{eq:loss_ratr}
\end{equation}

Equations~\eqref{eq:loss_intra}--\eqref{eq:loss_ratr} are complementary: the intra term stops two branches from ordering the most likely temporal correspondences the same way, and the inter term stops the same collapse on the harder negatives. Neither term drives the branches toward meaningless disagreement, because the reconstruction losses still tie every branch to the same target through MGFE.

\subsection{Symmetry Property of the Regularizer}
\label{subsec:symmetry_property}

The representation symmetry raised in Section~\ref{sec:introduction} has a concrete meaning in MgfrOFR. It is not a geometric symmetry of the image content but an invariance of the diversity objective under the group actions that relabel or exchange restoration branches. Two such invariances hold, and together they explain why the constraint is a symmetry principle rather than a balancing heuristic, the distinction we raise in Section~\ref{subsec:symmetry_ai}.

\textbf{Property 1 (Branch-permutation invariance).} Both the intra term in Equation~\eqref{eq:loss_intra} and the inter term $\mathcal{L}_{\text{inter}}$ sum the differentiable Kendall statistic over unordered branch pairs $g<g'$, and Equation~\eqref{eq:dktau} is symmetric in its arguments, $\mathrm{DKTau}(p,q;\tau)=\mathrm{DKTau}(q,p;\tau)$. Permuting the branch index of every descriptor by the same $\pi$ therefore leaves the regularizer unchanged:
\begin{equation}
\mathcal{L}_{\text{ratr}}\!\left(\{b^{(g)}\}_{g=0}^{G-1}\right)
=
\mathcal{L}_{\text{ratr}}\!\left(\{b^{(\pi(g))}\}_{g=0}^{G-1}\right),
\qquad
\forall\,\pi\in\mathcal{S}_G,
\label{eq:branch_permutation}
\end{equation}
where $\mathcal{S}_G$ is the symmetric group on the $G$ branches. In other words, $\mathcal{L}_{\text{ratr}}$ depends only on the unordered set of pairwise branch relations, not on any branch ordering or index. Since $\mathcal{S}_G$ has no privileged element, no branch can become dominant without leaving the orbit of objective-preserving relabelings.

\textbf{Property 2 (Direction-exchange invariance).} The two propagation streams enter the regularizer only through the average $B_t=\tfrac{1}{2}(B_t^{b}+B_t^{f})$ in Equation~\eqref{eq:mgfrofr_overview_2}, which is invariant under the $\mathbb{Z}_2$ action that swaps the backward and forward descriptors, $B_t^{b}\!\leftrightarrow\!B_t^{f}$. The objective thus treats the two temporal directions symmetrically and inherits the bidirectional symmetry of the backbone.

\textbf{Symmetry versus balancing.} These two invariances separate our constraint from a tuned balancing term. Balancing targets an \emph{outcome} (branches that end up contributing comparably) and is usually enforced by an asymmetric, hand-weighted penalty on individual branch magnitudes. RATR instead is built from group-invariant quantities ($\mathcal{S}_G$ on branches, $\mathbb{Z}_2$ on directions) and applies the identical constraint to every branch by construction. Balanced, complementary branches follow as a \emph{consequence} of optimizing this symmetric objective, not as a separately weighted goal.

\textbf{Scope of the claim.} The symmetry here is functional and representation-level: an invariance of the learning objective under permutation and exchange group actions, both standard symmetry principles in machine learning, rather than a visible geometric symmetry of the restored frames. We keep this reading deliberately narrow, and Section~\ref{subsec:symmetry_ai} places it against the broader use of symmetry in representation learning.

\subsection{Training Objective}
\label{subsec:training_objective}

The generator objective combines the standard old film restoration losses of the MambaOFR baseline with our ranking-aware regularizer. We use an $L_1$ pixel reconstruction loss $\mathcal{L}_{\mathrm{pix}}$, whose robustness for image restoration is analyzed in~\cite{zhao2017loss_restoration}, a VGG-based perceptual loss $\mathcal{L}_{\mathrm{perc}}$~\cite{johnson2016perceptual}, an adversarial loss $\mathcal{L}_{\mathrm{gan}}$~\cite{goodfellow2014gan}, and the ranking regularizer $\mathcal{L}_{\mathrm{ratr}}$:

\begin{equation}
\mathcal{L}_{\mathrm{total}} =
\mathcal{L}_{\mathrm{pix}}
+ \lambda_{\mathrm{perc}}\mathcal{L}_{\mathrm{perc}}
+ \lambda_{\mathrm{gan}}\mathcal{L}_{\mathrm{gan}}
+ \lambda_{\mathrm{ratr}}\mathcal{L}_{\mathrm{ratr}}.
\label{eq:loss_total}
\end{equation}

Because MGFE only augments the propagated feature stream and RATR is a pure auxiliary term, Equation~\eqref{eq:loss_total} slots into the baseline training loop without any other change. We set $\lambda_{\mathrm{perc}}=1.0$ and $\lambda_{\mathrm{gan}}=0.01$, following RTN~\cite{wan2022rtn} and MambaOFR~\cite{mao2025mambaofr}, and use $\lambda_{\mathrm{ratr}}=0.1$, $\lambda_{\mathrm{intra}}=1.0$, and $\lambda_{\mathrm{inter}}=0.5$ for the ranking term (see Section~\ref{subsec:sensitivity}). The smaller weight on $\mathcal{L}_{\text{inter}}$ reflects the coarser ordering signal from clip-centroid negatives. Unless stated otherwise, the full model uses feature dimension $C_f=16$, $G=3$ branches, $M=12$ restoration tokens, channel-wise average fusion in Equation~\eqref{eq:avg_fusion}, and a differentiable Kendall temperature $\tau=0.1$.
%% OFR_SEGMENT_END method
%% OFR_SEGMENT_BEGIN results d92408b65c8a74bed8a03b14e326d7f13fdf88e73c48c7a8280c2d041c08e903
\section{Experiments}
\label{sec:experiment}

We evaluate MgfrOFR under two complementary settings. Synthetic clips come with ground truth, which supports full-reference fidelity and perceptual metrics. Real archival footage lacks ground truth, so only no-reference naturalness metrics apply. We keep the two apart throughout this section, because a single merged score would mask the fidelity--naturalness trade-off that defines old film restoration.

\subsection{Datasets and Evaluation Metrics}
\label{subsec:datasets_metrics}

\subsubsection{Datasets}
\label{subsec:datasets}

We evaluate MgfrOFR on the SRWOV benchmark introduced with MambaOFR~\cite{mao2025mambaofr}, a dedicated benchmark for old film restoration that provides both synthetic and real-world test sets.

For training, we use the REDS training split~\cite{nah2019reds}, which contains 240 video sequences, each with 100 frames at $720 \times 1280$ resolution. Clean REDS frames are degraded on the fly using the synthetic degradation pipeline from MambaOFR, which simulates scratches, dust, blotches, flicker, and grain to produce paired degraded and clean training samples.

The synthetic test set holds 30 clips rendered with the same degradation pipeline on held-out REDS sequences. Each clip has 100 frames at $720 \times 1280$ with paired ground truth, which enables full-reference scoring. The real-world set holds 216 clips of archival footage from the 1920s to the 1960s, carrying authentic mixed degradations with no ground truth. We follow the original 216-clip SRWOV protocol~\cite{mao2025mambaofr}. It spans indoor portraits, newsreel footage, conversations, and multi-person scenes, and totals 29{,}256 frames for a broad naturalness assessment.

\subsubsection{Evaluation Metrics}
\label{subsec:eval_metrics}

Seven metrics cover three complementary dimensions. On synthetic data with ground truth, we report PSNR and SSIM~\cite{wang2004ssim} for pixel fidelity (higher is better), LPIPS~\cite{zhang2018lpips} for learned perceptual distance (lower is better), and DISTS~\cite{ding2020dists} for joint structure-texture similarity (lower is better). On real data without ground truth, we use NIQE~\cite{mittal2012niqe} and BRISQUE~\cite{mittal2012brisque} for statistical naturalness (lower is better), together with CLIP-IQA+~\cite{wang2023clipiqa}, which reads CLIP~\cite{radford2021clip} features through learnable quality-aware prompts (higher is better). The three groups probe pixel fidelity, perceptual quality, and naturalness in turn.

\subsection{Implementation Details}
\label{subsec:implementation}

\subsubsection{Training Details}
\label{subsubsec:training_details}

We train MgfrOFR on the REDS training split~\cite{nah2019reds} with the synthetic degradation pipeline from Section~\ref{subsec:datasets}. The optimizer is Adam~\cite{kingma2015adam} with $\beta_1=0.9$ and $\beta_2=0.99$, an initial learning rate of $2\times10^{-4}$, and a MultiStep schedule with milestones at 50K, 100K, and 150K iterations ($\gamma=0.5$). Training runs for $200$K iterations on $4$ NVIDIA A100 GPUs (80\,GB each), one clip per GPU per mini-batch. Each sample is $T=7$ consecutive frames cropped to $256\times256$. We use PyTorch 2.7 with CUDA 12.4 and fix the random seed to 42. At inference, RATR is off and frames run at full $720 \times 1280$ resolution without cropping.

\subsubsection{Baseline Adaptation Protocol}
\label{subsubsec:baseline_adaptation}

The comparison reuses released implementations and published settings in one unified environment. To keep it as fair as practical, we make each baseline's adaptation explicit along four axes.

\textbf{Retraining and computational budget.} Dedicated old film restoration methods (RTN, RRTN, MambaOFR) are retrained under the same REDS-based synthetic film degradation pipeline as MgfrOFR. In particular, MambaOFR---our primary baseline---and MgfrOFR are trained with an identical 200K-iteration schedule on the same A100-class hardware, so their computational budget for old film restoration adaptation is matched; RTN and RRTN are reproduced under the same degradation pipeline with a comparable training budget.

\textbf{Hyper-parameter tuning.} We retain each baseline's published architecture-specific hyper-parameters rather than performing exhaustive per-baseline re-tuning. Re-tuning every method to convergence on old film restoration would be computationally prohibitive and could itself bias the comparison toward whichever baseline received the most tuning effort.

\textbf{Degradation adaptation.} Generic video restoration methods (VRT, RVRT, ShiftNet) keep their published architecture and default optimization recipe; we replace only the task-specific degradation generation so that they can be trained on inputs for old film restoration, and we report them as faithfully reproduced references whose training budget follows each released recipe.

\textbf{Reference systems.} Enhancement-oriented methods (DeOldify, OldPhoto, DeepRemaster) are not designed for paired old film restoration and are not retrained on the old film restoration pipeline; we include them strictly as reference systems to contextualize perceptual trade-offs, not as task-matched old film restoration baselines.

The comparison is therefore a unified reproduction study under a shared degradation protocol, with a budget-matched tier for dedicated old film restoration methods. It is not a claim that every baseline has been exhaustively re-optimized for old film restoration.

\subsection{Comparison with State-of-the-Art}
\label{subsec:comparison_sota}

We compare MgfrOFR against nine baselines spanning dedicated old film restoration methods, general video restoration models, and image/video enhancement approaches. The dedicated old film restoration baselines are RTN~\cite{wan2022rtn}, RRTN~\cite{lin2024rrtn}, and MambaOFR~\cite{mao2025mambaofr}; the general video restoration baselines are VRT~\cite{liang2024vrt}, RVRT~\cite{liang2022rvrt}, and ShiftNet~\cite{li2023shiftnet}; and the enhancement-oriented references are DeOldify~\cite{jantic2019deoldify}, OldPhoto~\cite{wan2023oldphotopami}, and DeepRemaster~\cite{iizuka2019deepremaster}. No-reference metrics are computed using the pyiqa library under the same software environment.

\subsubsection{Quantitative Comparison on Synthetic Data}

On the SRWOV synthetic benchmark with full-reference metrics (Table~\ref{tab:sota}), MgfrOFR ranks first on all four full-reference metrics. It reaches 27.86~dB PSNR and improves on the same-protocol MambaOFR baseline by +1.02~dB with the final average-fusion configuration. The ranking matches the architectural gap between method families: generic video restoration models include no defect handling specific to old film restoration, while frame-wise enhancement methods can break temporal consistency.

\begin{table}[htbp]
\caption{Quantitative comparison reports SRWOV synthetic full-reference results under the unified reproduction protocol. Best results are shown in \bestres{red} and second-best results in \secondres{blue}.\label{tab:sota}}
\begin{tabularx}{\textwidth}{lCCCC}
\toprule
\textbf{Method} & \textbf{PSNR$\uparrow$} & \textbf{SSIM$\uparrow$} & \textbf{LPIPS$\downarrow$} & \textbf{DISTS$\downarrow$} \\
\midrule
ShiftNet~\cite{li2023shiftnet}          & 21.48 & 0.8234 & 0.2030 & 0.1303 \\
VRT~\cite{liang2024vrt}                 & 22.39 & 0.8631 & 0.1750 & 0.1087 \\
RVRT~\cite{liang2022rvrt}              & 22.43 & 0.8710 & 0.1655 & 0.1078 \\
DeOldify~\cite{jantic2019deoldify}      & 23.22 & 0.8923 & 0.2775 & 0.1260 \\
RRTN~\cite{lin2024rrtn}                & 24.15 & 0.9006 & 0.1082 & \secondres{0.0668} \\
OldPhoto~\cite{wan2023oldphotopami}     & 24.62 & 0.8524 & 0.2252 & 0.1144 \\
DeepRemaster~\cite{iizuka2019deepremaster} & 25.06 & \secondres{0.9185} & 0.1108 & 0.0895 \\
RTN~\cite{wan2022rtn}                   & 25.85 & 0.8869 & 0.1214 & 0.0862 \\
MambaOFR~\cite{mao2025mambaofr}        & \secondres{26.84} & 0.9153 & \secondres{0.0719} & 0.0733 \\
\midrule
MgfrOFR (Ours)                          & \bestres{27.86} & \bestres{0.9255} & \bestres{0.0600} & \bestres{0.0656} \\
\bottomrule
\end{tabularx}
\end{table}

A single average can hide clip-level variance, so we keep the paired, two-sided Wilcoxon signed-rank test over the 30 per-clip means as supporting evidence. For the final average-fusion configuration, MgfrOFR obtains significant paired improvements over MambaOFR on all four full-reference metrics (PSNR $p=3.73\times10^{-9}$; SSIM $p=1.73\times10^{-6}$; LPIPS $p=1.86\times10^{-9}$; DISTS $p=1.92\times10^{-6}$). The per-clip evidence also shows that PSNR and DISTS improve on 29 of 30 clips, while SSIM and LPIPS improve on all 30 clips.

\subsubsection{Quantitative Comparison on Real-World Data}

Table~\ref{tab:realworld} reports no-reference quality on the 216 real-world clips. None of them has a reference, and all methods share one pyiqa-based metric environment on the full 216-clip set. NIQE and BRISQUE measure statistical naturalness, while CLIP-IQA+ reflects CLIP-aligned perceptual quality; because they capture different attributes, we report each one individually instead of merging them into a single score.

\begin{table}[htbp]
\caption{Real-world evaluation reports no-reference quality metrics on SRWOV real footage under the same pyiqa-based metric environment. Best results are shown in \bestres{red} and second-best results in \secondres{blue}.\label{tab:realworld}}
\begin{tabularx}{\textwidth}{lCCC}
\toprule
\textbf{Method} & \textbf{NIQE$\downarrow$} & \textbf{BRISQUE$\downarrow$} & \textbf{CLIP-IQA+$\uparrow$} \\
\midrule
ShiftNet~\cite{li2023shiftnet}             & 5.71  & 42.82 & 0.3975 \\
VRT~\cite{liang2024vrt}                    & 5.66  & 42.73 & 0.3985 \\
RVRT~\cite{liang2022rvrt}                 & 5.72  & 42.64 & 0.4013 \\
DeOldify~\cite{jantic2019deoldify}         & 5.72  & 41.61 & 0.3768 \\
RRTN~\cite{lin2024rrtn}                   & 5.67  & 32.86 & 0.3969 \\
OldPhoto~\cite{wan2023oldphotopami}        & 6.56  & 30.45 & \bestres{0.4503} \\
DeepRemaster~\cite{iizuka2019deepremaster} & 5.99  & 40.62 & 0.3991 \\
RTN~\cite{wan2022rtn}                      & \secondres{5.17}  & \bestres{19.00} & 0.4163 \\
MambaOFR~\cite{mao2025mambaofr}           & 5.34  & 29.79 & \secondres{0.4351} \\
\midrule
MgfrOFR (Ours)                             & \bestres{5.12}  & \secondres{24.79} & 0.4092 \\
\bottomrule
\end{tabularx}
\end{table}

MgfrOFR gives the best NIQE (5.12) and the second-best BRISQUE (24.79) among all compared methods, improving over MambaOFR on both NIQE (5.12 vs.\ 5.34) and BRISQUE (24.79 vs.\ 29.79). Its CLIP-IQA+ (0.4092) remains below OldPhoto (0.4503), MambaOFR (0.4351), and RTN (0.4163). This gap is expected. CLIP-IQA+ rewards sharper, enhancement-oriented outputs, whereas our granularity recalibration stays conservative and favors statistical naturalness. We analyze this naturalness-versus-enhancement trade-off in Section~\ref{subsec:failure}.

\subsubsection{Qualitative Comparison}

Figure~\ref{fig:qualitative_synthetic} compares four representative REDS-synthetic scenes using full-frame degraded inputs and enlarged ROI crops. The colored boxes in the input row mark local regions, and the following rows compare the corresponding crops across restoration methods and the ground truth. The method families fail in different ways. General video restoration removes photometric degradation but leaves structured defects largely intact. Enhancement baselines raise contrast, yet blur or hallucinate local texture. RTN and MambaOFR clear many visible defects but still lose fine structure inside damaged regions. MgfrOFR stays closest to the ground-truth edges and texture around scratches, blotches, and high-contrast damage, while suppressing residual old-film artifacts. This matches the PSNR advantage in Table~\ref{tab:sota}. Supplementary Video~S1 provides side-by-side temporal comparisons in two parts: a synthetic part against the ground truth on REDS-synthetic clips with per-frame PSNR, followed by a real-world part on SRWOV archival clips annotated with the overall no-reference NIQE and BRISQUE.

\begin{figure}[!htbp]
\begin{adjustwidth}{-\extralength}{0cm}
\centering
\includegraphics[width=1.31\textwidth]{figures/Fig4_SOTA_Synthetic_REDS_synthetic_Qualitative.pdf}
\end{adjustwidth}
\caption{Qualitative comparison on four representative REDS-synthetic scenes. The top row shows full degraded input frames with colored ROI boxes, and the following rows compare enlarged ROI crops from DeOldify, OldPhoto, ShiftNet, VRT, RVRT, DeepRemaster, RTN, RRTN, MambaOFR, MgfrOFR (Ours), and the ground truth. The comparison illustrates that MgfrOFR better preserves local edges, scratches, and texture details while reducing visible old-film artifacts across the selected scenes.\label{fig:qualitative_synthetic}}
\end{figure}

Figure~\ref{fig:qualitative_realworld} compares three representative RealFilm-SRWOV real-world clips covering facial close-ups, indoor scenes, and high-contrast local structures. Because no ground truth is available, the comparison focuses on visible artifact suppression, structural preservation, naturalness, and local texture in the enlarged ROI crops. General video restoration clears part of the photometric degradation but leaves residual scratches, stains, or contrast shifts. Enhancement baselines sharpen texture, yet over-enhance faces, clothing, and high-contrast boundaries. MgfrOFR holds facial structure, fabric texture, object boundaries, and local contrast more consistently than MambaOFR and the other old film restoration baselines, and it suppresses residual old-film artifacts. These observations are consistent with the best NIQE and the MambaOFR-improved BRISQUE in Table~\ref{tab:realworld}, while CLIP-IQA+ reflects a separate sharpness-oriented trade-off. Two failure modes remain: MgfrOFR can over-smooth very fine texture under extreme degradation, and severe motion blur still causes flow-alignment errors, both examined in Section~\ref{subsec:failure}.

\begin{figure}[!htbp]
\begin{adjustwidth}{-\extralength}{0cm}
\centering
\includegraphics[width=1.31\textwidth]{figures/Fig5_SOTA_RealWorld_RealFilm_SRWOV_Qualitative.pdf}
\end{adjustwidth}
\caption{Qualitative comparison on three representative RealFilm-SRWOV real-world clips. The input row shows degraded frames with colored ROI boxes, and the following rows compare enlarged ROI crops from DeOldify, OldPhoto, DeepRemaster, ShiftNet, VRT, RVRT, RTN, RRTN, MambaOFR, and MgfrOFR (Ours). Colored boxes mark the selected ROI regions in the input frames, and the enlarged ROI crops compare local restoration details across methods. The comparison illustrates that MgfrOFR suppresses residual old-film artifacts while preserving natural structure and local texture without relying on ground-truth references.\label{fig:qualitative_realworld}}
\end{figure}

\FloatBarrier

\subsection{Ablation Study}
\label{subsec:ablation}

Table~\ref{tab:ablation} isolates the two contributions, MGFE recalibration and RATR regularization. These ablation values are used only for module analysis and do not replace the main comparison in Table~\ref{tab:sota}. Setting names match Figure~\ref{fig:ablation_visual}. The +RATR only row is a partial control: MGFE branch descriptors still serve as RATR ranking targets, but channel-wise recalibration is switched off.

\begin{table}[htbp]
\scriptsize
\caption{Ablation study on the SRWOV synthetic benchmark. The setting names follow Figure~\ref{fig:ablation_visual}, with max fusion retained as a tabular control; ``MGFE'' denotes channel-wise recalibration in this table. Best results are shown in \bestres{red} and second-best results in \secondres{blue}.\label{tab:ablation}}
\centering
\begin{adjustwidth}{-\extralength}{0cm}
\begingroup
\renewcommand{\arraystretch}{1.04}
\begin{tabularx}{\fulllength}{l*{6}{>{\centering\arraybackslash}X}}
\toprule
\textbf{Setting} & \textbf{MGFE} & \textbf{RATR} & \textbf{PSNR$\uparrow$} & \textbf{SSIM$\uparrow$} & \textbf{LPIPS$\downarrow$} & \textbf{DISTS$\downarrow$} \\
\midrule
MambaOFR baseline               & Off & Off & 26.84 & 0.9153 & 0.0719 & 0.0733 \\
+MGFE only                      & On  & Off & \secondres{27.75} & 0.9219 & 0.0651 & 0.0702 \\
+RATR only                      & Off & On  & 27.72 & \secondres{0.9246} & \secondres{0.0646} & \secondres{0.0696} \\
MgfrOFR (max-fusion control)   & On  & On  & 27.17 & 0.9168 & 0.0740 & 0.0773 \\
MgfrOFR (average fusion)       & On  & On  & \bestres{27.86} & \bestres{0.9255} & \bestres{0.0600} & \bestres{0.0656} \\
\bottomrule
\end{tabularx}
\endgroup
\end{adjustwidth}
\end{table}

\FloatBarrier

\noindent\textbf{Discussion.} Within this ablation protocol, the full model wins all four metrics and improves the MambaOFR baseline by +1.02~dB PSNR. Each component helps on its own, but neither is enough. MGFE-only recalibration lifts the baseline yet trails the full model on LPIPS and DISTS, so recalibration alone cannot reach the best fidelity--perception balance. RATR-only regularization matches that PSNR gain with a better perceptual balance than MGFE-only recalibration, which shows that ranking diversity pays off even before channel-wise feedback is enabled. Average fusion combines the two into the strongest result. The max-fusion control shows negative synergy on all four full-reference metrics and justifies average fusion as the default.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\textwidth]{figures/Fig6_Ablation_REDS_synthetic_Qualitative.jpg}
\caption{Visual ablation on REDS-based SRWOV synthetic data. \textbf{Top row:} full frames with red and green crop boxes marking the zoom regions. \textbf{Middle and bottom rows:} zoomed patches from the marked regions. The restoration columns compare the MambaOFR baseline, +MGFE only, +RATR only, and MgfrOFR with average fusion, with the degraded input and ground truth included as references. The max-fusion control is omitted for visual clarity. The comparison demonstrates that combining MGFE with RATR under average fusion yields the cleanest local restoration among the ablated configurations in Table~\ref{tab:ablation}.\label{fig:ablation_visual}}
\end{figure}

\subsection{Hyperparameter Sensitivity}
\label{subsec:sensitivity}

We report sensitivity and design-ablation entries only for configurations with complete evaluation records under the stated protocol. The main MgfrOFR configuration uses average restoration-token fusion, while the earlier max-fusion configuration is retained as a fusion control. Table~\ref{tab:sensitivity_granularity} covers granularity controls, a lower-temperature ranking control, token-insertion control, and branch-aggregation control. We treat the token-insertion and branch-aggregation settings as predefined max-fusion controls rather than alternatives to the average-fusion main configuration.

\begin{table}[H]
\caption{Sensitivity and design-control results on REDS synthetic data. The table combines a granularity sweep and fixed-size controls under the stated evaluation protocol; $M$ denotes the number of restoration tokens and $G$ denotes the number of granularity branches. MgfrOFR denotes the average-fusion main configuration, while the control rows are retained only for diagnostic comparison. Best results are shown in \bestres{red} and second-best results in \secondres{blue}.\label{tab:sensitivity_granularity}}
\centering
\begin{adjustwidth}{-\extralength}{0cm}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3.5pt}
\renewcommand{\arraystretch}{1.04}
\begin{tabularx}{\fulllength}{@{}>{\hsize=1.60\hsize\raggedright\arraybackslash}Xcc*{4}{>{\hsize=0.85\hsize\centering\arraybackslash}X}@{}}
\toprule
\textbf{Configuration} & \textbf{Tokens} & \textbf{Branches} & \textbf{PSNR$\uparrow$} & \textbf{SSIM$\uparrow$} & \textbf{LPIPS$\downarrow$} & \textbf{DISTS$\downarrow$} \\
\midrule
\multicolumn{7}{@{}l}{\textit{Granularity sweep}} \\
$G{=}1$, $M{=}4$                      & 4  & 1 & \bestres{27.95} & \bestres{0.9263} & 0.2153 & 0.1554 \\
$G{=}2$, $M{=}8$                      & 8  & 2 & 27.49 & 0.9211 & 0.2162 & 0.1557 \\
MgfrOFR (average fusion; $G{=}3$, $M{=}12$) & 12 & 3 & \secondres{27.86} & \secondres{0.9255} & \bestres{0.0600} & \bestres{0.0656} \\
$G{=}4$, $M{=}16$                     & 16 & 4 & 27.53 & 0.9197 & 0.2169 & 0.1565 \\
\addlinespace[1pt]
\midrule
\multicolumn{7}{@{}l}{\textit{Fixed 12-token / 3-branch controls}} \\
Lower ranking temperature ($\tau{=}0.05$) & 12 & 3 & 26.87 & 0.9177 & 0.0672 & 0.0717 \\
Prepend token insertion               & 12 & 3 & 27.61 & 0.9234 & \secondres{0.0627} & \secondres{0.0694} \\
Max branch aggregation                & 12 & 3 & 27.55 & 0.9223 & 0.0679 & 0.0730 \\
\bottomrule
\end{tabularx}
\endgroup
\end{adjustwidth}
\end{table}

The granularity controls expose a clear fidelity--perception split. The one-branch setting posts the highest PSNR and SSIM but much worse LPIPS and DISTS, so it overfits pixel fidelity and loses perceptual balance. The average-fusion main configuration is not the PSNR maximum. It is, however, the only setting here that pairs near-best fidelity with the best LPIPS and DISTS. The lower-temperature control stays competitive on LPIPS and DISTS but drops fidelity, so we keep $\tau=0.1$. The token-insertion and branch-aggregation controls both beat the max-fusion control on REDS synthetic data, yet neither overturns the average-fusion selection under the full-reference criterion. The max-aggregation control was also run on DAVIS synthetic data (26.4473 PSNR, 0.9067 SSIM, 0.0963 LPIPS, 0.0952 DISTS) and on RealFilm\_SRWOV (5.0988 NIQE, 26.1518 BRISQUE, 0.4268 CLIP-IQA+); these real-world values are mixed, so we report them as control-scope evidence rather than as a new main-configuration claim.

\FloatBarrier

\subsection{Complexity Analysis}
\label{subsec:complexity}

Table~\ref{tab:complexity} reports complexity on seven-frame $256{\times}256$ clips. The baseline rows and MgfrOFR row are measured under the same executable BasicOFR protocol on the L40 server (FP32, batch size 1, three warm-up and ten timed runs), which keeps the comparison auditable. The MgfrOFR row uses the final average-fusion configuration. FLOPs and latency are per seven-frame clip. The flow-based methods include the executable optical-flow front end; DeepRemaster uses none.

\begin{table}[htbp]
\caption{Computational complexity comparison under the L40 FP32 unified benchmark protocol ($1{\times}7{\times}3{\times}256{\times}256$, batch size 1, three warm-up and ten timed runs). The DeepRemaster/RTN/RRTN/MambaOFR baseline rows and the MgfrOFR row use the same executable BasicOFR protocol; the MgfrOFR row uses the final average-fusion configuration. Latency is reported per seven-frame clip.\label{tab:complexity}}
\begin{tabularx}{\textwidth}{lCCCCC}
\toprule
\textbf{Method} & \textbf{Params (M)} & \textbf{FLOPs (G)} & \textbf{Latency (ms/clip)$\downarrow$} & \textbf{FPS$\uparrow$} & \textbf{Peak Mem.\ (GB)$\downarrow$} \\
\midrule
DeepRemaster~\cite{iizuka2019deepremaster}   & 9.8781 & 914.0  & 17.9  & 391.6 & 0.35 \\
RTN~\cite{wan2022rtn}                        & 5.7351 & 2184.7 & 169.5 & 41.3  & 0.24 \\
RRTN~\cite{lin2024rrtn}                      & 7.0503 & 2782.2 & 298.4 & 23.5  & 0.75 \\
MambaOFR~\cite{mao2025mambaofr}              & 8.2984 & 2832.8 & 404.8 & 17.3  & 0.60 \\
\midrule
MgfrOFR (Ours)                              & 8.7540 & 3107.8 & 488.5 & 14.3  & 0.61 \\
\bottomrule
\end{tabularx}
\end{table}

A matched runtime benchmark isolates the cost of the proposed design: MgfrOFR adds only 0.012M parameters over the matched MambaOFR baseline (8.754M vs.\ 8.742M) and 14.094G FLOPs per seven-frame clip (3107.781G vs.\ 3093.687G). The baseline and MgfrOFR rows are reported under the same L40 FP32 measurement protocol, with runtime, FPS, and peak memory measured for the final MgfrOFR configuration.

\FloatBarrier
%% OFR_SEGMENT_END results
%% OFR_SEGMENT_BEGIN discussion 6d4e5ba261118a67e7c060c3cb04c9387bf2b9b188db07eccf65f9188cbba56e
\subsection{Analysis and Limitations}
\label{subsec:analysis_limitations}

\subsubsection{Comparison with the Closest Prior Work}
\label{subsec:vs_mambaofr}

MgfrOFR is built directly on top of MambaOFR~\cite{mao2025mambaofr}, so the contribution must be separated from the baseline backbone. We do not claim originality for bidirectional Mamba propagation, the degradation-aware prompt block, or the original reconstruction head. The contribution of this work lies in how propagated features are reorganized and regularized before reconstruction.

Compared with MambaOFR, MgfrOFR differs in four aspects. First, the propagated feature is no longer treated as a single restoration carrier; MGFE exposes explicit coarse-to-fine branches. Second, these branches are summarized and fed back through channel-wise recalibration rather than being used only for auxiliary supervision. Third, branch diversity is constrained by ranking correlation on temporal correspondences, rather than by an identity-based objective inherited from recognition tasks. Fourth, RATR is used only during training, so the deployment interface remains compatible with the baseline inference pipeline.

The key value of this design is representation-level symmetry. MgfrOFR does not treat object-level geometric regularity as the target; instead, it studies how an AI restoration model can maintain balanced coarse-to-fine feature spaces under asymmetric film degradation. MGFE separates evidence by restoration granularity, while RATR keeps temporal-similarity rankings from becoming redundant across branches. This provides a concrete symmetry-related mechanism without overstating the mathematical scope of the method.

\subsubsection{MGFE--RATR Synergy for Branch Balance}
\label{subsec:synergy}

The ablation study indicates that MGFE and RATR have different roles in the full model. RATR acts as a diversity regularizer that makes branches more complementary, while MGFE recalibration alone mainly improves fidelity (Table~\ref{tab:ablation}). In the RATR-only configuration, MGFE branch descriptors are still computed and used as multi-granularity ranking targets; only the channel-wise scale/shift feedback is disabled. MGFE therefore creates the branch structure needed for coarse-to-fine feature balance, whereas RATR suppresses redundant temporal-ranking behavior.

The asymmetric ablation behavior in Table~\ref{tab:ablation} shows that MGFE recalibration alone improves the baseline but does not reach the fidelity--perception balance of the full model. This is consistent with the perception--distortion trade-off~\cite{blau2018perception}, which establishes that optimizing a distortion measure such as PSNR does not by itself guarantee the best perceptual behavior. The channel-wise recalibration in Equation~\eqref{eq:recalibration} is conditioned on an averaged branch context and is driven mainly by the pixel reconstruction loss. Without a diversity constraint, the granularity branches can converge toward similar low-frequency corrections, so the MGFE-only variant remains less effective than the full model on LPIPS and DISTS. RATR mitigates this effect by acting on branch-ranking structure rather than on pixel error. Penalizing correlated temporal rankings across branches (Equations~\eqref{eq:loss_intra}--\eqref{eq:loss_ratr}) prevents the branches from collapsing onto a single fidelity-oriented direction and preserves complementary fine-grained evidence. The full model therefore gives the strongest combined fidelity and perceptual result.

The real-world results are consistent with this interpretation but do not prove content fidelity without ground truth. On the SRWOV real-world test set (Table~\ref{tab:realworld}), MgfrOFR achieves the best NIQE (5.12) and improves BRISQUE relative to MambaOFR (24.79 vs.\ 29.79), while RTN keeps the best BRISQUE score and MgfrOFR's CLIP-IQA+ (0.4092) is lower than OldPhoto, MambaOFR, and RTN. This pattern suggests that the multi-granularity decomposition transfers useful restoration structure beyond the synthetic training distribution, but the no-reference gains should be interpreted as evidence of statistical naturalness rather than definitive perceptual superiority.

\subsubsection{Branch Balance Analysis}
\label{subsec:branch_analysis}

To verify that the three granularity branches capture complementary restoration cues rather than correlated copies of the same evidence, we analyze the pairwise cosine similarity between branch descriptors across the SRWOV synthetic test set. This analysis directly tests the feature-space symmetry claim: balanced branches should remain comparable but not redundant.

The full model yields lower inter-branch similarity than the MGFE-only variant (Figures~\ref{fig:branch_similarity} and~\ref{fig:branch_error_map}), confirming that RATR is not just an auxiliary loss but the mechanism that keeps the granularity branches functionally distinct. The RATR-only variant remains closer to the full model than to MGFE-only, showing that ranking diversity regularization already suppresses collapse even before the recalibration feedback is enabled.

Figure~\ref{fig:branch_similarity} summarizes this contrast using the real 30-clip branch-similarity sweep. The heatmaps report the final 200K pairwise branch-similarity matrices, and the checkpoint curve reports mean off-diagonal similarity with standard deviation at 50K, 100K, 150K, and 200K iterations. In the MGFE-only configuration, the off-diagonal similarities remain high, indicating that the branches still encode nearly the same restoration evidence. In the full model, these off-diagonal values stay much lower across checkpoints, demonstrating that RATR produces a more differentiated and balanced branch geometry.

\begin{figure}[!t]
\centering
\includegraphics[width=0.98\textwidth]{figures/Fig9a_branch_similarity.pdf}
\caption{Branch balance analysis from the 30-clip REDS synthetic protocol. Panels (a) and (b) show the final 200K pairwise branch cosine-similarity matrices for the MGFE-only configuration and the full MgfrOFR model; panel (c) reports mean off-diagonal similarity with standard deviation over 30 clips across the 50K--200K checkpoints. At 200K, RATR reduces the mean off-diagonal similarity from $0.863\pm0.006$ to $0.261\pm0.143$, and final pairwise off-diagonal entries drop from 0.846--0.896 to 0.226--0.310. This confirms that ranking-aware regularization prevents granularity branches from collapsing into correlated descriptors.\label{fig:branch_similarity}}
\end{figure}

\begin{figure}[!t]
\centering
\includegraphics[width=0.98\textwidth]{figures/Fig9b_error_map.pdf}
\caption{Pixel-wise absolute-error comparison on four representative synthetic frames. The left and middle columns compare $|$MambaOFR $-$ GT$|$ and $|$MgfrOFR $-$ GT$|$; the right column illustrates their difference, where red indicates regions in which MgfrOFR reduces the reconstruction error. The error maps demonstrate that lower branch correlation translates into spatially broader restoration gains rather than isolated local fixes.\label{fig:branch_error_map}}
\end{figure}

Building on the similarity analysis, we qualitatively observe a consistent specialization pattern. The fine-grained branch is most sensitive to localized defects such as scratches and pixel-level noise; the coarse branch emphasizes broader structural corruption such as blotches and cracks; and the medium branch occupies an intermediate role. This behavior is consistent with progressive token fusion, where fewer surviving tokens aggregate over wider spatial support. The pixel-domain error maps in Figure~\ref{fig:branch_error_map} further demonstrate that this branch decorrelation translates into spatially broader restoration gains rather than isolated local fixes.

\subsubsection{When Does MgfrOFR Struggle?}
\label{subsec:failure}

MgfrOFR's advantage is not uniform across all degradation conditions. The ablation and sensitivity results indicate that the full model is most useful when heterogeneous degradation is present, such as structural damage co-occurring with fine scratches in the same frame. On clips dominated by a single degradation type, such as uniform flicker without spatial damage, the multi-granularity decomposition can add representational overhead without proportional benefit, and the baseline or RATR-only variant may match the full model's fidelity.

The real-world CLIP-IQA+ result highlights a trade-off between naturalness and enhancement-oriented perceptual quality. MgfrOFR's CLIP-IQA+ (0.4092) is below OldPhoto (0.4503), MambaOFR (0.4351), and RTN (0.4163), while MgfrOFR achieves the best NIQE (5.12) and improves BRISQUE relative to MambaOFR (24.79 vs.\ 29.79). This pattern reflects that different no-reference metrics measure distinct aspects of restoration quality. CLIP-IQA+ is trained on human quality annotations that correlate with sharp textures and high-contrast details~\cite{wang2023clipiqa}, favoring methods that enhance perceptual sharpness through learned global priors. NIQE and BRISQUE instead measure statistical deviation from natural image distributions and penalize artifacts introduced by texture hallucination. MgfrOFR's granularity-based recalibration operates conservatively on the propagated feature stream, which appears to preserve statistical naturalness while providing less texture enhancement than the stronger CLIP-IQA+ baselines. For archival restoration, NIQE/BRISQUE may be more relevant proxies when content fidelity is prioritized, but a human study is needed to validate that preference.

\subsubsection{Limitations, Threats to Validity, and Future Work}
\label{subsec:limitations}

\paragraph{Threats to Validity.}
Five threats affect the interpretation of the results. \textbf{Dataset threat}: all training uses synthetic degradation applied to REDS clips, which introduces a synthetic-to-real domain gap and may limit generalization to archival footage with correlated degradation chains not modeled by the pipeline. \textbf{Metric threat}: evaluation relies on PSNR/SSIM/LPIPS/DISTS for synthetic full-reference assessment and no-reference metrics for real-world assessment; these metrics emphasize different aspects of quality and may not fully align with human perceptual judgments. \textbf{Human-evaluation threat}: the study does not include an expert reader study with film-restoration practitioners or archivists, so the practical value of improvements on authentic footage is inferred from proxy metrics and qualitative inspection. \textbf{Baseline threat}: three baselines (VRT, RVRT, ShiftNet) required adaptation from video restoration to degradation specific to old film restoration, which preserves their architectures but may not reflect their optimal performance under a different training regime. \textbf{Synthetic-to-real threat}: the real-world evaluation lacks ground truth, so improvements in NIQE/BRISQUE reflect statistical naturalness rather than verified content fidelity, and the absence of external validation on additional datasets weakens the generalization claim.

\paragraph{Limitations and Future Work.}
RATR adds a training-time cost because it requires branch-wise similarity matrices over the batch-time descriptor set $\bar{N}=BT$. Its dominant cost therefore grows approximately quadratically in $\bar{N}$. Longer clips or larger effective batch-time products would make this quadratic term more pronounced, so gradient checkpointing or selective ranking construction, such as sampling a subset of anchors per iteration, will be needed for larger training settings. The second limitation is the synthetic-to-real domain gap caused by REDS-based training degradation. Although the real-world NIQE/BRISQUE results are encouraging, authentic archival footage can contain correlated degradation chains that synthetic pipelines do not model. The third limitation is evaluation scope: validation is limited to SRWOV, and additional archival datasets plus human evaluation would strengthen the generalization claim.

Promising extensions include adaptive branch activation conditioned on degradation severity, frequency-aware branch specialization that assigns structural recovery and texture restoration to dedicated branches, and joint old film restoration and colorization frameworks for archival digitization and cultural heritage restoration workflows~\cite{kokaram2004missing}.
%% OFR_SEGMENT_END discussion
%% OFR_SEGMENT_BEGIN conclusion 848760bf239a37401a9e19a3a6ce147881a84e9f7875de142d5297d6e29f8056
\section{Conclusions}
\label{sec:conclusion}

We presented MgfrOFR, a Mamba-based old film restoration framework that augments MambaOFR with explicit multi-granularity feature balancing. The Multi-Granularity Feature Extractor (MGFE) reorganizes propagated features into coarse-to-fine restoration-token branches and recalibrates the spatial stream through channel-wise feedback, while Ranking-Aware Triplet Regularization (RATR) discourages branch collapse by penalizing correlated temporal-similarity rankings during training.

With the final average-fusion configuration on the synthetic benchmark, MgfrOFR achieves the strongest full-reference scores among the tested baselines, improving PSNR by 1.02~dB over MambaOFR (27.86~dB vs.\ 26.84~dB). On 216 real-world archival clips, MgfrOFR obtains the lowest NIQE (5.12), improves BRISQUE over MambaOFR (24.79 vs.\ 29.79), and shows a lower CLIP-IQA+ value (0.4092) than the sharper enhancement-oriented and old film restoration baselines. Because the real-world setting lacks ground truth, these no-reference gains should be interpreted as evidence of improved statistical naturalness rather than definitive proof of perceptual superiority. The ablation study further shows that MGFE and RATR are complementary: MGFE alone improves the baseline but remains weaker than the full model on perceptual full-reference metrics, whereas the full model gives the best combined result when branch diversity is explicitly enforced through RATR and average fusion.

These results suggest that representation-level branch balance is a useful inductive bias for heterogeneous-degradation video restoration and practical archival digitization workflows. The main implication is that feature-space symmetry and temporally coordinated ranking behavior can improve restoration under degradation-induced asymmetry without changing the baseline inference interface. Several limitations remain: the method inherits the synthetic-to-real domain gap of REDS-based training; RATR adds a training-time cost that grows approximately quadratically with the batch-time descriptor set, increasing training time by approximately 7.6\% over MambaOFR under our setting; and evaluation is limited to the SRWOV benchmark and no-reference proxies on authentic footage. Future work will focus on adaptive branch activation conditioned on degradation severity, frequency-aware branch specialization that assigns structural recovery and texture restoration to dedicated branches, lighter ranking constructions such as selective anchor sampling, human-in-the-loop evaluation, and broader validation on additional archival benchmarks.
%% OFR_SEGMENT_END conclusion
```

### `evidence/gptpro-polish-20260708-grammar-references/04_FROZEN_numbers.md`

```markdown
# FROZEN Numbers

| normalized | kind | expected_count | raw | anchors |
|---|---|---:|---|---|
| `74` | `generic` | 3 | `74` | 01_manuscript_current_full.tex:1, 01_manuscript_current_full.tex:24, 01_manuscript_current_full.tex:422 |
| `80130941` | `generic` | 1 | `80130941` | 01_manuscript_current_full.tex:1 |
| `4` | `generic` | 11 | `4` | 01_manuscript_current_full.tex:1, related_work:38, 01_manuscript_current_full.tex:59, 01_manuscript_current_full.tex:59, method:261, results:451, results:534, results:601, results:606, results:606, results:609 |
| `12` | `generic` | 11 | `12` | 01_manuscript_current_full.tex:1, method:138, method:155, method:161, method:420, results:608, results:608, results:612, results:613, results:614, results:615 |
| `2772` | `generic` | 1 | `2772` | 01_manuscript_current_full.tex:1 |
| `75326` | `generic` | 1 | `75326` | 01_manuscript_current_full.tex:1 |
| `8543` | `generic` | 1 | `8543` | 01_manuscript_current_full.tex:1 |
| `82` | `generic` | 1 | `82` | 01_manuscript_current_full.tex:1 |
| `332` | `generic` | 1 | `332` | 01_manuscript_current_full.tex:1 |
| `21965` | `generic` | 1 | `21965` | 01_manuscript_current_full.tex:1 |
| `86378903` | `generic` | 1 | `86378903` | 01_manuscript_current_full.tex:1 |
| `34` | `generic` | 1 | `34` | 01_manuscript_current_full.tex:4 |
| `3` | `generic` | 18 | `3` | 01_manuscript_current_full.tex:4, related_work:31, related_work:31, method:80, method:138, method:155, method:161, method:161, method:257, method:420, results:608, results:612, results:613, results:614, results:615, results:632, 01_manuscript_current_full.tex:651, 01_manuscript_current_full.tex:714 |
| `0` | `generic` | 13 | `0` | 01_manuscript_current_full.tex:4, method:168, method:177, method:179, method:220, method:230, method:343, method:391, method:393, results:532, results:542, results:560, results:596 |
| `65` | `generic` | 3 | `65` | 01_manuscript_current_full.tex:4, 01_manuscript_current_full.tex:422, 01_manuscript_current_full.tex:651 |
| `8988` | `generic` | 1 | `8988` | 01_manuscript_current_full.tex:4 |
| `45` | `generic` | 1 | `45` | 01_manuscript_current_full.tex:4 |
| `7` | `generic` | 7 | `7` | 01_manuscript_current_full.tex:4, 01_manuscript_current_full.tex:422, 01_manuscript_current_full.tex:422, results:451, results:605, results:612, results:632 |
| `087` | `generic` | 1 | `087` | 01_manuscript_current_full.tex:4 |
| `3955` | `generic` | 1 | `3955` | 01_manuscript_current_full.tex:4 |
| `03562` | `generic` | 1 | `03562` | 01_manuscript_current_full.tex:4 |
| `85` | `generic` | 1 | `85` | 01_manuscript_current_full.tex:4 |
| `56` | `generic` | 2 | `56` | 01_manuscript_current_full.tex:4, 01_manuscript_current_full.tex:651 |
| `485` | `generic` | 1 | `485` | 01_manuscript_current_full.tex:4 |
| `50400` | `generic` | 1 | `50400` | 01_manuscript_current_full.tex:4 |
| `9` | `generic` | 6 | `9` | 01_manuscript_current_full.tex:4, 01_manuscript_current_full.tex:59, method:155, 01_manuscript_current_full.tex:651, discussion:684, discussion:690 |
| `2019` | `generic` | 12 | `2019` | introduction:8, related_work:31, related_work:33, results:436, results:451, results:471, results:471, results:486, results:489, results:513, results:516, results:637 |
| `2022` | `generic` | 14 | `2022` | introduction:10, related_work:31, related_work:33, related_work:33, related_work:38, related_work:45, method:420, results:471, results:471, results:485, results:490, results:512, results:517, results:638 |
| `2024` | `generic` | 19 | `2024` | introduction:10, introduction:10, introduction:10, related_work:31, related_work:31, related_work:33, related_work:33, related_work:33, related_work:33, related_work:38, related_work:38, related_work:38, results:471, results:471, results:484, results:487, results:511, results:514, results:639 |
| `2025` | `generic` | 16 | `2025` | introduction:10, introduction:12, related_work:31, related_work:38, related_work:40, related_work:45, method:73, method:157, method:420, results:434, results:438, results:471, results:491, results:518, results:640, discussion:658 |
| `2017` | `generic` | 3 | `2017` | introduction:12, related_work:45, method:409 |
| `2021` | `generic` | 5 | `2021` | introduction:12, related_work:33, related_work:45, related_work:55, results:443 |
| `2018` | `generic` | 8 | `2018` | introduction:12, introduction:12, related_work:45, related_work:45, related_work:55, method:246, results:443, discussion:669 |
| `72` | `generic` | 1 | `72` | 01_manuscript_current_full.tex:24 |
| `8` | `generic` | 6 | `8` | 01_manuscript_current_full.tex:24, 01_manuscript_current_full.tex:24, 01_manuscript_current_full.tex:422, 01_manuscript_current_full.tex:422, results:607, results:607 |
| `693` | `generic` | 1 | `693` | 01_manuscript_current_full.tex:24 |
| `2` | `generic` | 47 | `2` | 01_manuscript_current_full.tex:24, related_work:38, related_work:38, related_work:45, related_work:45, related_work:50, related_work:55, method:97, method:98, method:101, method:114, method:137, method:159, method:161, method:163, method:168, method:168, method:177, method:177, method:179, method:179, method:179, method:198, method:198, method:203, method:203, method:236, method:236, method:236, method:261, method:265, method:292, method:296, method:329, method:335, method:349, method:363, method:400, method:400, method:400, method:400, method:402, 01_manuscript_current_full.tex:422, results:451, results:451, results:607, 01_manuscript_current_full.tex:651 |
| `2806` | `generic` | 1 | `2806` | 01_manuscript_current_full.tex:24 |
| `409` | `generic` | 1 | `409` | 01_manuscript_current_full.tex:24 |
| `727` | `generic` | 1 | `727` | 01_manuscript_current_full.tex:24 |
| `474` | `generic` | 1 | `474` | 01_manuscript_current_full.tex:24 |
| `1` | `generic` | 41 | `1` | 01_manuscript_current_full.tex:24, 01_manuscript_current_full.tex:24, 01_manuscript_current_full.tex:59, method:66, method:66, method:73, method:79, method:97, method:105, method:106, method:107, method:109, method:114, method:119, method:155, method:155, method:155, method:179, method:209, method:210, method:215, method:220, method:230, method:241, method:246, method:288, method:307, method:315, method:335, method:336, method:349, method:363, method:364, method:389, method:400, method:409, results:451, results:529, results:606, results:610, results:632 |
| `5031296` | `generic` | 1 | `5031296` | 01_manuscript_current_full.tex:24 |
| `40` | `generic` | 4 | `40` | 01_manuscript_current_full.tex:24, results:629, results:632, results:647 |
| `722` | `generic` | 1 | `722` | 01_manuscript_current_full.tex:24 |
| `2004` | `generic` | 3 | `2004` | related_work:31, results:443, discussion:712 |
| `2007` | `generic` | 1 | `2007` | related_work:31 |
| `2013` | `generic` | 1 | `2013` | related_work:31 |
| `2020` | `generic` | 3 | `2020` | related_work:50, related_work:55, results:443 |
| `2023` | `generic` | 10 | `2023` | related_work:50, method:253, results:443, results:471, results:471, results:483, results:488, results:510, results:515, discussion:701 |
| `06` | `generic` | 1 | `06` | 01_manuscript_current_full.tex:59 |
| `19` | `generic` | 1 | `19` | 01_manuscript_current_full.tex:59 |
| `0708604` | `generic` | 1 | `0708604` | 01_manuscript_current_full.tex:59 |
| `523` | `generic` | 1 | `523` | 01_manuscript_current_full.tex:59 |
| `5312` | `generic` | 1 | `5312` | 01_manuscript_current_full.tex:59 |
| `15095` | `generic` | 1 | `15095` | 01_manuscript_current_full.tex:59 |
| `51662` | `generic` | 1 | `51662` | 01_manuscript_current_full.tex:59 |
| `0.02` | `generic` | 1 | `0.02` | method:149 |
| `-1` | `generic` | 10 | `-1` | method:159, method:161, method:163, method:168, method:177, method:179, method:220, method:230, method:391, method:393 |
| `0.1` | `generic` | 3 | `0.1` | method:242, method:246, method:343 |
| `10%` | `generic` | 1 | `10%` | method:246 |
| `1938` | `generic` | 1 | `1938` | method:253 |
| `2016` | `generic` | 1 | `2016` | method:409 |
| `2014` | `generic` | 1 | `2014` | method:409 |
| `1.0` | `generic` | 1 | `1.0` | method:420 |
| `0.5` | `generic` | 2 | `0.5` | method:420, results:451 |
| `92408` | `generic` | 1 | `92408` | 01_manuscript_current_full.tex:422 |
| `03` | `generic` | 1 | `03` | 01_manuscript_current_full.tex:422 |
| `14e326` | `generic` | 1 | `14e326` | 01_manuscript_current_full.tex:422 |
| `13` | `generic` | 1 | `13` | 01_manuscript_current_full.tex:422 |
| `88e73` | `generic` | 1 | `88e73` | 01_manuscript_current_full.tex:422 |
| `48` | `generic` | 1 | `48` | 01_manuscript_current_full.tex:422 |
| `8280` | `generic` | 1 | `8280` | 01_manuscript_current_full.tex:422 |
| `041` | `generic` | 1 | `041` | 01_manuscript_current_full.tex:422 |
| `08e903` | `generic` | 1 | `08e903` | 01_manuscript_current_full.tex:422 |
| `240` | `generic` | 1 | `240` | results:436 |
| `100` | `generic` | 6 | `100` | results:436, results:438, results:451, results:451, results:458, discussion:680 |
| `720x` | `generic` | 3 | `720x` | results:436, results:438, results:451 |
| `1280` | `generic` | 3 | `1280` | results:436, results:438, results:451 |
| `30` | `generic` | 7 | `30` | results:438, results:498, results:498, results:498, discussion:680, discussion:685, discussion:685 |
| `216` | `generic` | 5 | `216` | results:438, results:438, results:502, results:502, conclusion:720 |
| `1920` | `generic` | 1 | `1920` | results:438 |
| `1960` | `generic` | 1 | `1960` | results:438 |
| `29` | `generic` | 2 | `29` | results:438, results:498 |
| `256` | `generic` | 5 | `256` | results:438, results:451, results:629, results:629, results:632 |
| `2012` | `generic` | 2 | `2012` | results:443, results:443 |
| `2015` | `generic` | 1 | `2015` | results:451 |
| `0.9` | `generic` | 1 | `0.9` | results:451 |
| `50` | `generic` | 3 | `50` | results:451, discussion:680, discussion:685 |
| `150` | `generic` | 2 | `150` | results:451, discussion:680 |
| `200` | `generic` | 6 | `200` | results:451, results:458, discussion:680, discussion:680, discussion:685, discussion:685 |
| `80` | `generic` | 1 | `80` | results:451 |
| `2.7` | `generic` | 1 | `2.7` | results:451 |
| `12.4` | `generic` | 1 | `12.4` | results:451 |
| `27.86` | `generic` | 5 | `27.86dB` | results:475, results:493, results:571, results:608, conclusion:720 |
| `+1.02dB` | `generic` | 2 | `+1.02dB` | results:475, results:580 |
| `21.48` | `generic` | 1 | `21.48` | results:483 |
| `0.8234` | `generic` | 1 | `0.8234` | results:483 |
| `0.2030` | `generic` | 1 | `0.2030` | results:483 |
| `0.1303` | `generic` | 1 | `0.1303` | results:483 |
| `22.39` | `generic` | 1 | `22.39` | results:484 |
| `0.8631` | `generic` | 1 | `0.8631` | results:484 |
| `0.1750` | `generic` | 1 | `0.1750` | results:484 |
| `0.1087` | `generic` | 1 | `0.1087` | results:484 |
| `22.43` | `generic` | 1 | `22.43` | results:485 |
| `0.8710` | `generic` | 1 | `0.8710` | results:485 |
| `0.1655` | `generic` | 1 | `0.1655` | results:485 |
| `0.1078` | `generic` | 1 | `0.1078` | results:485 |
| `23.22` | `generic` | 1 | `23.22` | results:486 |
| `0.8923` | `generic` | 1 | `0.8923` | results:486 |
| `0.2775` | `generic` | 1 | `0.2775` | results:486 |
| `0.1260` | `generic` | 1 | `0.1260` | results:486 |
| `24.15` | `generic` | 1 | `24.15` | results:487 |
| `0.9006` | `generic` | 1 | `0.9006` | results:487 |
| `0.1082` | `generic` | 1 | `0.1082` | results:487 |
| `0.0668` | `generic` | 1 | `0.0668` | results:487 |
| `24.62` | `generic` | 1 | `24.62` | results:488 |
| `0.8524` | `generic` | 1 | `0.8524` | results:488 |
| `0.2252` | `generic` | 1 | `0.2252` | results:488 |
| `0.1144` | `generic` | 1 | `0.1144` | results:488 |
| `25.06` | `generic` | 1 | `25.06` | results:489 |
| `0.9185` | `generic` | 1 | `0.9185` | results:489 |
| `0.1108` | `generic` | 1 | `0.1108` | results:489 |
| `0.0895` | `generic` | 1 | `0.0895` | results:489 |
| `25.85` | `generic` | 1 | `25.85` | results:490 |
| `0.8869` | `generic` | 1 | `0.8869` | results:490 |
| `0.1214` | `generic` | 1 | `0.1214` | results:490 |
| `0.0862` | `generic` | 1 | `0.0862` | results:490 |
| `26.84` | `generic` | 3 | `26.84` | results:491, results:567, conclusion:720 |
| `0.9153` | `generic` | 2 | `0.9153` | results:491, results:567 |
| `0.0719` | `generic` | 2 | `0.0719` | results:491, results:567 |
| `0.0733` | `generic` | 2 | `0.0733` | results:491, results:567 |
| `0.9255` | `generic` | 3 | `0.9255` | results:493, results:571, results:608 |
| `0.0600` | `generic` | 3 | `0.0600` | results:493, results:571, results:608 |
| `0.0656` | `generic` | 3 | `0.0656` | results:493, results:571, results:608 |
| `3.73e-9` | `generic` | 1 | `3.73e-9` | results:498 |
| `1.73e-6` | `generic` | 1 | `1.73e-6` | results:498 |
| `1.86e-9` | `generic` | 1 | `1.86e-9` | results:498 |
| `1.92e-6` | `generic` | 1 | `1.92e-6` | results:498 |
| `5.71` | `generic` | 1 | `5.71` | results:510 |
| `42.82` | `generic` | 1 | `42.82` | results:510 |
| `0.3975` | `generic` | 1 | `0.3975` | results:510 |
| `5.66` | `generic` | 1 | `5.66` | results:511 |
| `42.73` | `generic` | 1 | `42.73` | results:511 |
| `0.3985` | `generic` | 1 | `0.3985` | results:511 |
| `5.72` | `generic` | 2 | `5.72` | results:512, results:513 |
| `42.64` | `generic` | 1 | `42.64` | results:512 |
| `0.4013` | `generic` | 1 | `0.4013` | results:512 |
| `41.61` | `generic` | 1 | `41.61` | results:513 |
| `0.3768` | `generic` | 1 | `0.3768` | results:513 |
| `5.67` | `generic` | 1 | `5.67` | results:514 |
| `32.86` | `generic` | 1 | `32.86` | results:514 |
| `0.3969` | `generic` | 1 | `0.3969` | results:514 |
| `6.56` | `generic` | 1 | `6.56` | results:515 |
| `30.45` | `generic` | 1 | `30.45` | results:515 |
| `0.4503` | `generic` | 3 | `0.4503` | results:515, results:525, discussion:701 |
| `5.99` | `generic` | 1 | `5.99` | results:516 |
| `40.62` | `generic` | 1 | `40.62` | results:516 |
| `0.3991` | `generic` | 1 | `0.3991` | results:516 |
| `5.17` | `generic` | 1 | `5.17` | results:517 |
| `19.00` | `generic` | 1 | `19.00` | results:517 |
| `0.4163` | `generic` | 3 | `0.4163` | results:517, results:525, discussion:701 |
| `5.34` | `generic` | 2 | `5.34` | results:518, results:525 |
| `29.79` | `generic` | 5 | `29.79` | results:518, results:525, discussion:671, discussion:701, conclusion:720 |
| `0.4351` | `generic` | 3 | `0.4351` | results:518, results:525, discussion:701 |
| `5.12` | `generic` | 6 | `5.12` | results:520, results:525, results:525, discussion:671, discussion:701, conclusion:720 |
| `24.79` | `generic` | 6 | `24.79` | results:520, results:525, results:525, discussion:671, discussion:701, conclusion:720 |
| `0.4092` | `generic` | 5 | `0.4092` | results:520, results:525, discussion:671, discussion:701, conclusion:720 |
| `1.31` | `generic` | 2 | `1.31` | results:534, results:544 |
| `5` | `generic` | 1 | `5` | results:544 |
| `1.04` | `generic` | 2 | `1.04` | results:562, results:600 |
| `6` | `generic` | 4 | `6` | results:563, results:584, 01_manuscript_current_full.tex:651, 01_manuscript_current_full.tex:714 |
| `27.75` | `generic` | 1 | `27.75` | results:568 |
| `0.9219` | `generic` | 1 | `0.9219` | results:568 |
| `0.0651` | `generic` | 1 | `0.0651` | results:568 |
| `0.0702` | `generic` | 1 | `0.0702` | results:568 |
| `27.72` | `generic` | 1 | `27.72` | results:569 |
| `0.9246` | `generic` | 1 | `0.9246` | results:569 |
| `0.0646` | `generic` | 1 | `0.0646` | results:569 |
| `0.0696` | `generic` | 1 | `0.0696` | results:569 |
| `27.17` | `generic` | 1 | `27.17` | results:570 |
| `0.9168` | `generic` | 1 | `0.9168` | results:570 |
| `0.0740` | `generic` | 1 | `0.0740` | results:570 |
| `0.0773` | `generic` | 1 | `0.0773` | results:570 |
| `0.95` | `generic` | 1 | `0.95` | results:584 |
| `3.5` | `generic` | 1 | `3.5` | results:599 |
| `1.60` | `generic` | 1 | `1.60` | results:601 |
| `0.85` | `generic` | 1 | `0.85` | results:601 |
| `27.95` | `generic` | 1 | `27.95` | results:606 |
| `0.9263` | `generic` | 1 | `0.9263` | results:606 |
| `0.2153` | `generic` | 1 | `0.2153` | results:606 |
| `0.1554` | `generic` | 1 | `0.1554` | results:606 |
| `27.49` | `generic` | 1 | `27.49` | results:607 |
| `0.9211` | `generic` | 1 | `0.9211` | results:607 |
| `0.2162` | `generic` | 1 | `0.2162` | results:607 |
| `0.1557` | `generic` | 1 | `0.1557` | results:607 |
| `16` | `generic` | 2 | `16` | results:609, results:609 |
| `27.53` | `generic` | 1 | `27.53` | results:609 |
| `0.9197` | `generic` | 1 | `0.9197` | results:609 |
| `0.2169` | `generic` | 1 | `0.2169` | results:609 |
| `0.1565` | `generic` | 1 | `0.1565` | results:609 |
| `0.05` | `generic` | 1 | `0.05` | results:613 |
| `26.87` | `generic` | 1 | `26.87` | results:613 |
| `0.9177` | `generic` | 1 | `0.9177` | results:613 |
| `0.0672` | `generic` | 1 | `0.0672` | results:613 |
| `0.0717` | `generic` | 1 | `0.0717` | results:613 |
| `27.61` | `generic` | 1 | `27.61` | results:614 |
| `0.9234` | `generic` | 1 | `0.9234` | results:614 |
| `0.0627` | `generic` | 1 | `0.0627` | results:614 |
| `0.0694` | `generic` | 1 | `0.0694` | results:614 |
| `27.55` | `generic` | 1 | `27.55` | results:615 |
| `0.9223` | `generic` | 1 | `0.9223` | results:615 |
| `0.0679` | `generic` | 1 | `0.0679` | results:615 |
| `0.0730` | `generic` | 1 | `0.0730` | results:615 |
| `26.4473` | `generic` | 1 | `26.4473` | results:622 |
| `0.9067` | `generic` | 1 | `0.9067` | results:622 |
| `0.0963` | `generic` | 1 | `0.0963` | results:622 |
| `0.0952` | `generic` | 1 | `0.0952` | results:622 |
| `5.0988` | `generic` | 1 | `5.0988` | results:622 |
| `26.1518` | `generic` | 1 | `26.1518` | results:622 |
| `0.4268` | `generic` | 1 | `0.4268` | results:622 |
| `32` | `generic` | 2 | `32` | results:632, results:647 |
| `9.8781` | `generic` | 1 | `9.8781` | results:637 |
| `914.0` | `generic` | 1 | `914.0` | results:637 |
| `17.9` | `generic` | 1 | `17.9` | results:637 |
| `391.6` | `generic` | 1 | `391.6` | results:637 |
| `0.35` | `generic` | 1 | `0.35` | results:637 |
| `5.7351` | `generic` | 1 | `5.7351` | results:638 |
| `2184.7` | `generic` | 1 | `2184.7` | results:638 |
| `169.5` | `generic` | 1 | `169.5` | results:638 |
| `41.3` | `generic` | 1 | `41.3` | results:638 |
| `0.24` | `generic` | 1 | `0.24` | results:638 |
| `7.0503` | `generic` | 1 | `7.0503` | results:639 |
| `2782.2` | `generic` | 1 | `2782.2` | results:639 |
| `298.4` | `generic` | 1 | `298.4` | results:639 |
| `23.5` | `generic` | 1 | `23.5` | results:639 |
| `0.75` | `generic` | 1 | `0.75` | results:639 |
| `8.2984` | `generic` | 1 | `8.2984` | results:640 |
| `2832.8` | `generic` | 1 | `2832.8` | results:640 |
| `404.8` | `generic` | 1 | `404.8` | results:640 |
| `17.3` | `generic` | 1 | `17.3` | results:640 |
| `0.60` | `generic` | 1 | `0.60` | results:640 |
| `8.7540` | `generic` | 1 | `8.7540` | results:642 |
| `3107.8` | `generic` | 1 | `3107.8` | results:642 |
| `488.5` | `generic` | 1 | `488.5` | results:642 |
| `14.3` | `generic` | 1 | `14.3` | results:642 |
| `0.61` | `generic` | 1 | `0.61` | results:642 |
| `0.012` | `generic` | 1 | `0.012` | results:647 |
| `8.754` | `generic` | 1 | `8.754` | results:647 |
| `8.742` | `generic` | 1 | `8.742` | results:647 |
| `14.094` | `generic` | 1 | `14.094` | results:647 |
| `3107.781` | `generic` | 1 | `3107.781` | results:647 |
| `3093.687` | `generic` | 1 | `3093.687` | results:647 |
| `4e5` | `generic` | 1 | `4e5` | 01_manuscript_current_full.tex:651 |
| `261118` | `generic` | 1 | `261118` | 01_manuscript_current_full.tex:651 |
| `67e7` | `generic` | 1 | `67e7` | 01_manuscript_current_full.tex:651 |
| `060` | `generic` | 1 | `060` | 01_manuscript_current_full.tex:651 |
| `04` | `generic` | 1 | `04` | 01_manuscript_current_full.tex:651 |
| `9387` | `generic` | 1 | `9387` | 01_manuscript_current_full.tex:651 |
| `188` | `generic` | 1 | `188` | 01_manuscript_current_full.tex:651 |
| `07` | `generic` | 1 | `07` | 01_manuscript_current_full.tex:651 |
| `9188` | `generic` | 1 | `9188` | 01_manuscript_current_full.tex:651 |
| `0.98` | `generic` | 2 | `0.98` | discussion:684, discussion:690 |
| `-200` | `generic` | 1 | `-200` | discussion:685 |
| `0.863` | `generic` | 1 | `0.863` | discussion:685 |
| `0.006` | `generic` | 1 | `0.006` | discussion:685 |
| `0.261` | `generic` | 1 | `0.261` | discussion:685 |
| `0.846` | `generic` | 1 | `0.846` | discussion:685 |
| `-0.896` | `generic` | 1 | `-0.896` | discussion:685 |
| `0.226` | `generic` | 1 | `0.226` | discussion:685 |
| `848760` | `generic` | 1 | `848760` | 01_manuscript_current_full.tex:714 |
| `239` | `generic` | 1 | `239` | 01_manuscript_current_full.tex:714 |
| `37401` | `generic` | 1 | `37401` | 01_manuscript_current_full.tex:714 |
| `9e19` | `generic` | 1 | `9e19` | 01_manuscript_current_full.tex:714 |
| `147881` | `generic` | 1 | `147881` | 01_manuscript_current_full.tex:714 |
| `84e9` | `generic` | 1 | `84e9` | 01_manuscript_current_full.tex:714 |
| `7875` | `generic` | 1 | `7875` | 01_manuscript_current_full.tex:714 |
| `142` | `generic` | 1 | `142` | 01_manuscript_current_full.tex:714 |
| `5297` | `generic` | 1 | `5297` | 01_manuscript_current_full.tex:714 |
| `6e29` | `generic` | 1 | `6e29` | 01_manuscript_current_full.tex:714 |
| `8056` | `generic` | 1 | `8056` | 01_manuscript_current_full.tex:714 |
| `1.02` | `generic` | 1 | `1.02dB` | conclusion:720 |
| `7.6%` | `generic` | 1 | `7.6%` | conclusion:722 |
```

### `evidence/gptpro-polish-20260708-grammar-references/02_reference_citation_report.md`

```markdown
# Reference and Citation Report

Generated from current `source/MGFROFR.tex`, `source/sections/*.tex`, and `source/references.bib`.

- Unique cited keys: 48
- BibTeX entries: 48
- Missing cited keys: 0
- Unused BibTeX entries: 0

## Gate Result

PASS: every BibTeX entry is cited exactly as part of the current manuscript citation set, and every cited key exists in `references.bib`.

## Cited References

| key | year | venue/source | DOI/URL present | title |
|---|---:|---|---|---|
| `blau2018perception` | 2018 | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition | yes | The Perception-Distortion Tradeoff |
| `chan2021basicvsr` | 2021 | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition | yes | {BasicVSR}: The Search for Essential Components in Video Super-Resolution and Beyond |
| `chan2022basicvsrpp` | 2022 | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition | yes | {BasicVSR++}: Improving Video Super-Resolution with Enhanced Propagation and Alignment |
| `chen2020mocov2` | 2020 |  | yes | Improved Baselines with Momentum Contrastive Learning |
| `dabov2007bm3d` | 2007 | IEEE Transactions on Image Processing | yes | Image Denoising by Sparse {3-D} Transform-Domain Collaborative Filtering |
| `ding2020dists` | 2022 | IEEE Transactions on Pattern Analysis and Machine Intelligence | yes | Image Quality Assessment: Unifying Structure and Texture Similarity |
| `goodfellow2014gan` | 2014 | Advances in Neural Information Processing Systems (NeurIPS) | yes | Generative Adversarial Nets |
| `gu2022s4` | 2022 | International Conference on Learning Representations (ICLR) | yes | Efficiently Modeling Long Sequences with Structured State Spaces |
| `gu2024mamba` | 2024 | Conference on Language Modeling (COLM) | yes | Mamba: Linear-Time Sequence Modeling with Selective State Spaces |
| `gu2025reidmamba` | 2026 | IEEE Transactions on Multimedia | yes | {ReIDMamba}: Learning Discriminative Features with Visual State Space Model for Person Re-Identification |
| `guo2024mambair` | 2024 | European Conference on Computer Vision (ECCV) | yes | {MambaIR}: A Simple Baseline for Image Restoration with State-Space Model |
| `he2013guided` | 2013 | IEEE Transactions on Pattern Analysis and Machine Intelligence | yes | Guided Image Filtering |
| `iizuka2019deepremaster` | 2019 | ACM Transactions on Graphics | yes | {DeepRemaster}: Temporal Source-Reference Attention Networks for Comprehensive Video Enhancement |
| `jantic2019deoldify` | 2019 |  | no | DeOldify |
| `johnson2016perceptual` | 2016 | European Conference on Computer Vision (ECCV) | yes | Perceptual Losses for Real-Time Style Transfer and Super-Resolution |
| `kendall1938measure` | 1938 | Biometrika | yes | A New Measure of Rank Correlation |
| `kingma2015adam` | 2015 | International Conference on Learning Representations (ICLR) | yes | Adam: A Method for Stochastic Optimization |
| `kokaram2004missing` | 2004 | IEEE Transactions on Image Processing | yes | On Missing Data Treatment for Degraded Video and Film Archives: {A} Survey and a New {Bayesian} Approach |
| `li2023shiftnet` | 2023 | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | A Simple Baseline for Video Restoration with Grouped Spatial-Temporal Shift |
| `liang2022rvrt` | 2022 | Neural Information Processing Systems (NeurIPS) | yes | Recurrent Video Restoration Transformer with Guided Deformable Attention |
| `liang2024vrt` | 2024 | IEEE Transactions on Image Processing | yes | {VRT}: A Video Restoration Transformer |
| `lin2017fpn` | 2017 | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | Feature Pyramid Networks for Object Detection |
| `lin2024diffbir` | 2024 | European Conference on Computer Vision (ECCV) | yes | {DiffBIR}: Toward Blind Image Restoration with Generative Diffusion Prior |
| `lin2024rrtn` | 2024 | Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision | yes | Restoring Degraded Old Films with Recursive Recurrent Transformer Networks |
| `liu2024vmamba` | 2024 | Neural Information Processing Systems (NeurIPS) | yes | {VMamba}: Visual State Space Model |
| `mao2025mambaofr` | 2025 | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | {MambaOFR}: Old Film Restoration with State Space Model |
| `mittal2012brisque` | 2012 | IEEE Transactions on Image Processing | yes | No-Reference Image Quality Assessment in the Spatial Domain |
| `mittal2012niqe` | 2013 | IEEE Signal Processing Letters | yes | Making a ``Completely Blind'' Image Quality Analyzer |
| `nah2019reds` | 2019 | IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) | yes | {NTIRE} 2019 Challenge on Video Deblurring and Super-Resolution: Dataset and Study |
| `perez2018film` | 2018 | AAAI Conference on Artificial Intelligence | yes | {FiLM}: Visual Reasoning with a General Conditioning Layer |
| `qian2020multiview_matrix_correlation` | 2020 | Journal of Electronic Imaging | yes | Multiview Feature Fusion Optimization Method for Image Retrieval Based on Matrix Correlation |
| `radford2021clip` | 2021 | Proceedings of the 38th International Conference on Machine Learning (ICML) | yes | Learning Transferable Visual Models from Natural Language Supervision |
| `sun2018pcb` | 2018 | European Conference on Computer Vision (ECCV) | yes | Beyond Part Models: Person Retrieval with Refined Part Pooling |
| `tran2025vsrm` | 2025 | IEEE/CVF International Conference on Computer Vision (ICCV) | yes | {VSRM}: A Robust Mamba-Based Framework for Video Super-Resolution |
| `wan2022rtn` | 2022 | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | Bringing Old Films Back to Life |
| `wan2023oldphotopami` | 2023 | IEEE Transactions on Pattern Analysis and Machine Intelligence | yes | Old Photo Restoration via Deep Latent Space Translation |
| `wang2004ssim` | 2004 | IEEE Transactions on Image Processing | yes | Image Quality Assessment: From Error Visibility to Structural Similarity |
| `wang2018mgn` | 2018 | ACM International Conference on Multimedia (MM) | yes | Learning Discriminative Features with Multiple Granularities for Person Re-Identification |
| `wang2019edvr` | 2019 | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops | yes | {EDVR}: Video Restoration with Enhanced Deformable Convolutional Networks |
| `wang2021hrnet` | 2021 | IEEE Transactions on Pattern Analysis and Machine Intelligence | yes | Deep High-Resolution Representation Learning for Visual Recognition |
| `wang2023clipiqa` | 2023 | AAAI Conference on Artificial Intelligence | yes | Exploring {CLIP} for Assessing the Look and Feel of Images |
| `wu2024seesr` | 2024 | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | {SeeSR}: Towards Semantics-Aware Real-World Image Super-Resolution |
| `yu2021multiview_tensor_fusion` | 2021 | IEEE Access | yes | A Multi-View Fusion Method via Tensor Learning and Gradient Descent for Image Features |
| `yu2024supir` | 2024 | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild |
| `zamir2022mirnetv2` | 2023 | IEEE Transactions on Pattern Analysis and Machine Intelligence | yes | Learning Enriched Features for Fast Image Restoration and Enhancement |
| `zhang2018lpips` | 2018 | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) | yes | The Unreasonable Effectiveness of Deep Features as a Perceptual Metric |
| `zhao2017loss_restoration` | 2017 | IEEE Transactions on Computational Imaging | yes | Loss Functions for Image Restoration With Neural Networks |
| `zheng2023diffkendall` | 2023 | Neural Information Processing Systems (NeurIPS) | yes | {DiffKendall}: A Novel Approach for Few-Shot Learning with Differentiable {Kendall's} Rank Correlation |
```

### `source/references.bib`

```text


@inproceedings{wang2019edvr,
  author = {Wang, Xintao and Chan, Kelvin C.K. and Yu, Ke and Dong, Chao and Loy, Chen Change},
  title = {{EDVR}: Video Restoration with Enhanced Deformable Convolutional Networks},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops},
  year = {2019},
  pages = {1954--1963},
  doi = {10.1109/CVPRW.2019.00247}
}

@inproceedings{chan2021basicvsr,
  author = {Chan, Kelvin C.K. and Wang, Xintao and Yu, Ke and Dong, Chao and Loy, Chen Change},
  title = {{BasicVSR}: The Search for Essential Components in Video Super-Resolution and Beyond},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year = {2021},
  pages = {4945--4954},
  doi = {10.1109/CVPR46437.2021.00491}
}

@inproceedings{chan2022basicvsrpp,
  author = {Chan, Kelvin C.K. and Zhou, Shangchen and Xu, Xiangyu and Loy, Chen Change},
  title = {{BasicVSR++}: Improving Video Super-Resolution with Enhanced Propagation and Alignment},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  year = {2022},
  pages = {5962--5971},
  doi = {10.1109/CVPR52688.2022.00588}
}

@inproceedings{wan2022rtn,
  author = {Wan, Ziyu and Zhang, Bo and Li, Dongdong and Liu, Yingfu and Chen, Jing and Loy, Chen Change},
  title = {Bringing Old Films Back to Life},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2022},
  pages = {17694--17703},
  doi = {10.1109/CVPR52688.2022.01717},
  publisher = {IEEE},
  address = {New York, NY, USA}
}

@inproceedings{lin2024rrtn,
  author = {Lin, Shan and Simo-Serra, Edgar},
  title = {Restoring Degraded Old Films with Recursive Recurrent Transformer Networks},
  booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  year = {2024},
  pages = {6704--6714},
  doi = {10.1109/WACV57701.2024.00658}
}

@inproceedings{mao2025mambaofr,
  author = {Mao, Tianyu and Zhang, Lei and Wan, Ziyu and Li, Guanglu and Loy, Chen Change},
  title = {{MambaOFR}: Old Film Restoration with State Space Model},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2025},
  pages = {4622--4630},
  doi = {10.1109/CVPR52734.2025.02611},
  publisher = {IEEE},
  address = {New York, NY, USA}
}


@article{liang2024vrt,
  author = {Liang, Jingyun and Cao, Jingzhang and Fan, Yuchen and Zhang, Kai and Ranjan, Rakesh and Li, Yawei and Timofte, Radu and {Van Gool}, Luc},
  title = {{VRT}: A Video Restoration Transformer},
  journal = {IEEE Transactions on Image Processing},
  year = {2024},
  volume = {33},
  pages = {2171--2182},
  doi = {10.1109/TIP.2024.3372454}
}

@inproceedings{liang2022rvrt,
  author = {Liang, Jingyun and Fan, Yuchen and Xiang, Xinyu and Ranjan, Rakesh and Ilg, Eddy and Green, Simon and Cao, Jingzhang and Zhang, Kai and Timofte, Radu and {Van Gool}, Luc},
  title = {Recurrent Video Restoration Transformer with Guided Deformable Attention},
  booktitle = {Neural Information Processing Systems (NeurIPS)},
  year = {2022},
  pages = {378--393},
  eprint = {2206.02146},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {Curran Associates, Inc.},
  address = {Red Hook, NY, USA},
  doi = {10.52202/068431-0028}
}


@inproceedings{gu2024mamba,
  author = {Gu, Albert and Dao, Tri},
  title = {Mamba: Linear-Time Sequence Modeling with Selective State Spaces},
  booktitle = {Conference on Language Modeling (COLM)},
  year = {2024},
  url = {https://openreview.net/forum?id=tEYskw1VY2},
  eprint = {2312.00752},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  note = {Published at COLM 2024; OpenReview venue page used as canonical landing page}
}

@inproceedings{guo2024mambair,
  author = {Guo, Hang and Li, Jinwei and Dai, Tao and Ouyang, Zhiyuan and Ren, Xiaowei and Xia, Shu-Tao},
  title = {{MambaIR}: A Simple Baseline for Image Restoration with State-Space Model},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year = {2024},
  pages = {222--241},
  eprint = {2402.15648},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {Springer},
  address = {Cham, Switzerland},
  doi = {10.1007/978-3-031-72649-1_13}
}

@inproceedings{lin2017fpn,
  author = {Lin, Tsung-Yi and Doll{\'a}r, Piotr and Girshick, Ross and He, Kaiming and Hariharan, Bharath and Belongie, Serge},
  title = {Feature Pyramid Networks for Object Detection},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2017},
  pages = {936--944},
  doi = {10.1109/CVPR.2017.106},
  publisher = {IEEE},
  address = {New York, NY, USA}
}

@article{gu2025reidmamba,
  author = {Gu, Hongyang and Yang, Qisong and Pu, Lei and Han, Siming and Ding, Yao},
  title = {{ReIDMamba}: Learning Discriminative Features with Visual State Space Model for Person Re-Identification},
  journal = {IEEE Transactions on Multimedia},
  year = {2026},
  doi = {10.1109/TMM.2026.3668499},
  eprint = {2511.07948},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV}
}

@inproceedings{zheng2023diffkendall,
  author = {Zheng, Zhedong and Zheng, Liang and Yang, Yi},
  title = {{DiffKendall}: A Novel Approach for Few-Shot Learning with Differentiable {Kendall's} Rank Correlation},
  booktitle = {Neural Information Processing Systems (NeurIPS)},
  year = {2023},
  pages = {72895--72913},
  eprint = {2307.09007},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {Curran Associates, Inc.},
  address = {Red Hook, NY, USA},
  doi = {10.52202/075280-2149}
}

@article{kendall1938measure,
  author = {Kendall, Maurice G.},
  title = {A New Measure of Rank Correlation},
  journal = {Biometrika},
  year = {1938},
  volume = {30},
  number = {1/2},
  pages = {81--93},
  doi = {10.2307/2332226}
}

@article{iizuka2019deepremaster,
  author = {Iizuka, Satoshi and Simo-Serra, Edgar},
  title = {{DeepRemaster}: Temporal Source-Reference Attention Networks for Comprehensive Video Enhancement},
  journal = {ACM Transactions on Graphics},
  year = {2019},
  volume = {38},
  number = {6},
  pages = {1--13},
  doi = {10.1145/3355089.3356570}
}

@misc{jantic2019deoldify,
  author = {Antic, Jason},
  title = {DeOldify},
  year = {2019},
  howpublished = {\url{https://github.com/jantic/DeOldify}},
  note = {GitHub repository; available online (accessed on 1 April 2026)}
}

@inproceedings{li2023shiftnet,
  author = {Li, Dasong and Zhang, Yi and Cheung, Ka Chun and Wang, Xiangyu and Qin, Hongwei and Li, Hongsheng},
  title = {A Simple Baseline for Video Restoration with Grouped Spatial-Temporal Shift},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2023},
  pages = {9822--9832},
  doi = {10.1109/CVPR52729.2023.00947},
  publisher = {IEEE},
  address = {New York, NY, USA}
}







@inproceedings{liu2024vmamba,
  author = {Liu, Yue and Tian, Yunjie and Zhao, Yuzhong and Yu, Xinhai and Xie, Lingxi and Wang, Yanzhao and Ye, Qixiang and Liu, Yun},
  title = {{VMamba}: Visual State Space Model},
  booktitle = {Neural Information Processing Systems (NeurIPS)},
  year = {2024},
  pages = {103089--103122},
  eprint = {2401.10166},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {Curran Associates, Inc.},
  address = {Red Hook, NY, USA},
  doi = {10.52202/079017-3273}
}


@inproceedings{sun2018pcb,
  author = {Sun, Yifan and Zheng, Liang and Yang, Yi and Tian, Qi and Wang, Shengjin},
  title = {Beyond Part Models: Person Retrieval with Refined Part Pooling},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year = {2018},
  pages = {480--496},
  doi = {10.1007/978-3-030-01225-0_30},
  publisher = {Springer},
  address = {Cham, Switzerland}
}

@inproceedings{wang2018mgn,
  author = {Wang, Guansong and Yuan, Yufei and Chen, Xiong and Li, Jiwei and Zhou, Xi},
  title = {Learning Discriminative Features with Multiple Granularities for Person Re-Identification},
  booktitle = {ACM International Conference on Multimedia (MM)},
  year = {2018},
  pages = {274--282},
  doi = {10.1145/3240508.3240552},
  publisher = {ACM},
  address = {New York, NY, USA}
}

@misc{chen2020mocov2,
  author = {Chen, Xinlei and Fan, Haoqi and Girshick, Ross and He, Kaiming},
  title = {Improved Baselines with Momentum Contrastive Learning},
  year = {2020},
  eprint = {2003.04297},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  url = {https://arxiv.org/abs/2003.04297},
  note = {Use arXiv abs page as canonical landing page}
}

@inproceedings{johnson2016perceptual,
  author = {Johnson, Justin and Alahi, Alexandre and Li, Fei-Fei},
  title = {Perceptual Losses for Real-Time Style Transfer and Super-Resolution},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year = {2016},
  pages = {694--711},
  doi = {10.1007/978-3-319-46475-6_43},
  publisher = {Springer},
  address = {Cham, Switzerland}
}

@inproceedings{goodfellow2014gan,
  author = {Goodfellow, Ian and Pouget-Abadie, Jean and Mirza, Mehdi and Xu, Bing and Warde-Farley, David and Ozair, Sherjil and Courville, Aaron and Bengio, Yoshua},
  title = {Generative Adversarial Nets},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  year = {2014},
  volume = {27},
  pages = {2672--2680},
  publisher = {Curran Associates, Inc.},
  url = {https://proceedings.neurips.cc/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html},
  note = {Canonical NeurIPS proceedings page}
}

@inproceedings{zhang2018lpips,
  author = {Zhang, Richard and Isola, Phillip and Efros, Alexei A. and Shechtman, Eli and Wang, Oliver},
  title = {The Unreasonable Effectiveness of Deep Features as a Perceptual Metric},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2018},
  pages = {586--595},
  doi = {10.1109/CVPR.2018.00068},
  publisher = {IEEE},
  address = {New York, NY, USA}
}

@article{ding2020dists,
  author = {Ding, Keyan and Ma, Kede and Wang, Shiqian and Simoncelli, Eero P.},
  title = {Image Quality Assessment: Unifying Structure and Texture Similarity},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year = {2022},
  volume = {44},
  number = {9},
  pages = {2567--2581},
  doi = {10.1109/TPAMI.2020.3045810}
}

@article{mittal2012niqe,
  author = {Mittal, Anish and Soundararajan, Rajiv and Bovik, Alan C.},
  title = {Making a ``Completely Blind'' Image Quality Analyzer},
  journal = {IEEE Signal Processing Letters},
  year = {2013},
  volume = {20},
  number = {3},
  pages = {209--212},
  doi = {10.1109/LSP.2012.2227726}
}

@article{mittal2012brisque,
  author = {Mittal, Anish and Moorthy, Anush Krishna and Bovik, Alan Conrad},
  title = {No-Reference Image Quality Assessment in the Spatial Domain},
  journal = {IEEE Transactions on Image Processing},
  year = {2012},
  volume = {21},
  number = {12},
  pages = {4695--4708},
  doi = {10.1109/TIP.2012.2214050}
}

@inproceedings{wang2023clipiqa,
  author = {Wang, Jianyi and Chan, Kelvin C.K. and Loy, Chen Change},
  title = {Exploring {CLIP} for Assessing the Look and Feel of Images},
  booktitle = {AAAI Conference on Artificial Intelligence},
  year = {2023},
  pages = {2555--2563},
  doi = {10.1609/aaai.v37i2.25353},
  publisher = {AAAI},
  address = {Washington, DC, USA}
}

@article{wang2004ssim,
  author = {Wang, Zhou and Bovik, Alan C. and Sheikh, Hamid R. and Simoncelli, Eero P.},
  title = {Image Quality Assessment: From Error Visibility to Structural Similarity},
  journal = {IEEE Transactions on Image Processing},
  year = {2004},
  volume = {13},
  number = {4},
  pages = {600--612},
  doi = {10.1109/TIP.2003.819861}
}

@inproceedings{nah2019reds,
  author = {Nah, Seungjun and Baik, Sungyong and Hong, Seokil and Moon, Gyeongsik and Son, Sanghyun and Timofte, Radu and Lee, Kyoung Mu},
  title = {{NTIRE} 2019 Challenge on Video Deblurring and Super-Resolution: Dataset and Study},
  booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)},
  year = {2019},
  pages = {1996--2005},
  doi = {10.1109/CVPRW.2019.00251},
  publisher = {IEEE},
  address = {New York, NY, USA}
}


@inproceedings{kingma2015adam,
  author = {Kingma, Diederik P. and Ba, Jimmy},
  title = {Adam: A Method for Stochastic Optimization},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2015},
  eprint = {1412.6980},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  note = {Published at ICLR 2015; OpenReview venue page used as canonical landing page},
  url = {https://openreview.net/forum?id=8gmWwjFyLj}
}



@inproceedings{gu2022s4,
  author = {Gu, Albert and Goel, Karan and R{\'e}, Christopher},
  title = {Efficiently Modeling Long Sequences with Structured State Spaces},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year = {2022},
  eprint = {2111.00396},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  note = {Published at ICLR 2022 (Oral); OpenReview venue page used as canonical landing page},
  url = {https://openreview.net/forum?id=uYLFoz1vlAC}
}





@inproceedings{tran2025vsrm,
  author = {Tran, Dinh Phu and Dao, Duy Hung and Kim, Daeyoung},
  title = {{VSRM}: A Robust Mamba-Based Framework for Video Super-Resolution},
  booktitle = {IEEE/CVF International Conference on Computer Vision (ICCV)},
  year = {2025},
  eprint = {2501.02498},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {IEEE},
  address = {New York, NY, USA},
  doi = {10.1109/iccv51701.2025.01365}
}

@inproceedings{lin2024diffbir,
  author = {Lin, Xinqi and He, Jingwen and Chen, Ziyan and Lyu, Zhaoyang and Dai, Bo and Yu, Fanghua and Qiao, Yu and Ouyang, Wanli and Dong, Chao},
  title = {{DiffBIR}: Toward Blind Image Restoration with Generative Diffusion Prior},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year = {2024},
  doi = {10.1007/978-3-031-73202-7_25},
  url = {https://mlanthology.org/eccv/2024/lin2024eccv-diffbir/}
}

@inproceedings{yu2024supir,
  author = {Yu, Fanghua and Gu, Jinjin and Li, Zheyuan and Hu, Jinfan and Kong, Xiangtao and Wang, Xintao and He, Jingwen and Qiao, Yu and Dong, Chao},
  title = {Scaling Up to Excellence: Practicing Model Scaling for Photo-Realistic Image Restoration In the Wild},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2024},
  pages = {25669--25680},
  url = {https://openaccess.thecvf.com/content/CVPR2024/html/Yu_Scaling_Up_to_Excellence_Practicing_Model_Scaling_for_Photo-Realistic_Image_CVPR_2024_paper.html}
}

@inproceedings{wu2024seesr,
  author = {Wu, Rongyuan and Yang, Tao and Sun, Lingchen and Zhang, Zhengqiang and Li, Shuai and Zhang, Lei},
  title = {{SeeSR}: Towards Semantics-Aware Real-World Image Super-Resolution},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2024},
  pages = {25456--25467},
  url = {https://openaccess.thecvf.com/content/CVPR2024/html/Wu_SeeSR_Towards_Semantics-Aware_Real-World_Image_Super-Resolution_CVPR_2024_paper.html}
}




@inproceedings{radford2021clip,
  title = {Learning Transferable Visual Models from Natural Language Supervision},
  author = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},
  booktitle = {Proceedings of the 38th International Conference on Machine Learning (ICML)},
  pages = {8748--8763},
  year = {2021},
  volume = {139},
  series = {Proceedings of Machine Learning Research},
  eprint = {2103.00020},
  archivePrefix = {arXiv},
  primaryClass = {cs.CV},
  publisher = {PMLR},
  url = {https://proceedings.mlr.press/v139/radford21a.html},
  note = {Canonical PMLR proceedings page}
}




@article{yu2021multiview_tensor_fusion,
  author = {Yu, L. and Zhang, D. and Liu, N. and Zhou, W.},
  title = {A Multi-View Fusion Method via Tensor Learning and Gradient Descent for Image Features},
  journal = {IEEE Access},
  year = {2021},
  volume = {9},
  pages = {79389--79399},
  doi = {10.1109/ACCESS.2021.3079499}
}


@article{qian2020multiview_matrix_correlation,
  author = {Qian, D. and Yu, L. and Tang, H. and Zhao, J.},
  title = {Multiview Feature Fusion Optimization Method for Image Retrieval Based on Matrix Correlation},
  journal = {Journal of Electronic Imaging},
  year = {2020},
  volume = {29},
  pages = {053007},
  doi = {10.1117/1.JEI.29.5.053007}
}




@inproceedings{perez2018film,
  author = {Perez, Ethan and Strub, Florian and de Vries, Harm and Dumoulin, Vincent and Courville, Aaron},
  title = {{FiLM}: Visual Reasoning with a General Conditioning Layer},
  booktitle = {AAAI Conference on Artificial Intelligence},
  year = {2018},
  doi = {10.1609/aaai.v32i1.11671},
  publisher = {AAAI},
  address = {Washington, DC, USA}
}

%=====================================================================
% Additional journal references (HRNet/OldPhoto journal versions,
% restoration & vision surveys, classical restoration baselines).
%=====================================================================

@article{wang2021hrnet,
  author = {Wang, Jingdong and Sun, Ke and Cheng, Tianheng and Jiang, Borui and Deng, Chaorui and Zhao, Yang and Liu, Dong and Mu, Yadong and Tan, Mingkui and Wang, Xinggang and Liu, Wenyu and Xiao, Bin},
  title = {Deep High-Resolution Representation Learning for Visual Recognition},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year = {2021},
  volume = {43},
  number = {10},
  pages = {3349--3364},
  doi = {10.1109/TPAMI.2020.2983686}
}

@article{wan2023oldphotopami,
  author = {Wan, Ziyu and Zhang, Bo and Chen, Dongdong and Zhang, Pan and Chen, Dong and Liao, Jing and Wen, Fang},
  title = {Old Photo Restoration via Deep Latent Space Translation},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year = {2023},
  volume = {45},
  number = {2},
  pages = {2071--2087},
  doi = {10.1109/TPAMI.2022.3163183}
}

@article{zamir2022mirnetv2,
  author = {Zamir, Syed Waqas and Arora, Aditya and Khan, Salman and Hayat, Munawar and Khan, Fahad Shahbaz and Yang, Ming-Hsuan and Shao, Ling},
  title = {Learning Enriched Features for Fast Image Restoration and Enhancement},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year = {2023},
  volume = {45},
  number = {2},
  pages = {1934--1948},
  doi = {10.1109/TPAMI.2022.3167175}
}

@article{kokaram2004missing,
  author = {Kokaram, Anil C.},
  title = {On Missing Data Treatment for Degraded Video and Film Archives: {A} Survey and a New {Bayesian} Approach},
  journal = {IEEE Transactions on Image Processing},
  year = {2004},
  volume = {13},
  number = {3},
  pages = {397--415},
  doi = {10.1109/TIP.2004.823815}
}

@inproceedings{blau2018perception,
  author = {Blau, Yochai and Michaeli, Tomer},
  title = {The Perception-Distortion Tradeoff},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  year = {2018},
  pages = {6228--6237},
  doi = {10.1109/CVPR.2018.00652}
}

@article{zhao2017loss_restoration,
  author = {Zhao, Hang and Gallo, Orazio and Frosio, Iuri and Kautz, Jan},
  title = {Loss Functions for Image Restoration With Neural Networks},
  journal = {IEEE Transactions on Computational Imaging},
  year = {2017},
  volume = {3},
  number = {1},
  pages = {47--57},
  doi = {10.1109/TCI.2016.2644865}
}

@article{dabov2007bm3d,
  author = {Dabov, Kostadin and Foi, Alessandro and Katkovnik, Vladimir and Egiazarian, Karen},
  title = {Image Denoising by Sparse {3-D} Transform-Domain Collaborative Filtering},
  journal = {IEEE Transactions on Image Processing},
  year = {2007},
  volume = {16},
  number = {8},
  pages = {2080--2095},
  doi = {10.1109/TIP.2007.901238}
}




@article{he2013guided,
  author = {He, Kaiming and Sun, Jian and Tang, Xiaoou},
  title = {Guided Image Filtering},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year = {2013},
  volume = {35},
  number = {6},
  pages = {1397--1409},
  doi = {10.1109/TPAMI.2012.213}
}
```
