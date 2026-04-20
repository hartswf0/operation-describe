# Source: Readout Guidance: Learning Control from Diffusion Features

> **Species**: source_summary  
> **Scale**: fragment  
> **Source Index**: 63  
> **Type**: article  
> **Evidence Grade**: C (article/blog)  
> **Author(s)**: Luo, Grace; Darrell, Trevor; Wang, Oliver; Goldman, Dan B.  
> **Year**: 2024  
> **Last Processed**: 2026-04-13  

---

## Abstract / Summary

We present Readout Guidance, a method for controlling text-to-image diffusion models with learned signals. Readout Guidance uses readout heads, lightweight networks trained to extract signals from the features of a pre-trained, frozen diffusion model at every timestep. These readouts can encode single-image properties, such as pose, depth, and edges; or higher-order properties that relate multiple images, such as correspondence and appearance similarity. Furthermore, by comparing the readout estimates to a user-defined target, and back-propagating the gradient through the readout head, these estimates can be used to guide the sampling process. Compared to prior methods for conditional generation, Readout Guidance requires significantly fewer added parameters and training samples, and offer

## World Effects

**Relevant Worlds**: [[world-latent-space]]

## Cosmological Role

This source contributes evidence to the latent space domain of the cosmos.
