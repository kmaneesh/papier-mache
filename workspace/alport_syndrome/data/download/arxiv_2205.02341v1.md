# Soft Syndrome Decoding of Quantum LDPC Codes for Joint Correction of Data and Syndrome Errors

**arXiv ID**: 2205.02341v1
**Authors**: Nithin Raveendran, Narayanan Rengaswamy, Asit Kumar Pradhan, Bane Vasić
**Published**: 2022-05-04T22:00:32Z
**PDF Link**: https://arxiv.org/pdf/2205.02341v1

## Abstract
Quantum errors are primarily detected and corrected using the measurement of syndrome information which itself is an unreliable step in practical error correction implementations. Typically, such faulty or noisy syndrome measurements are modeled as a binary measurement outcome flipped with some probability. However, the measured syndrome is in fact a discretized value of the continuous voltage or current values obtained in the physical implementation of the syndrome extraction. In this paper, we use this "soft" or analog information without the conventional discretization step to benefit the iterative decoders for decoding quantum low-density parity-check (QLDPC) codes. Syndrome-based iterative belief propagation decoders are modified to utilize the syndrome-soft information to successfully correct both data and syndrome errors simultaneously, without repeated measurements. We demonstrate the advantages of extracting the soft information from the syndrome in our improved decoders, not only in terms of comparison of thresholds and logical error rates for quasi-cyclic lifted-product QLDPC code families, but also for faster convergence of iterative decoders. In particular, the new BP decoder with noisy syndrome performs as good as the standard BP decoder under ideal syndrome.
