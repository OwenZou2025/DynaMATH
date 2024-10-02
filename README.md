# DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models

This repository contains the code for our ICLR 2025 submission: **DynaMath: A Dynamic Visual Benchmark for Evaluating Mathematical Reasoning Robustness of Vision Language Models**.

## 🌟 About DynaMath

The rapid advancements in Vision-Language Models (VLMs) have shown significant potential in tackling mathematical reasoning tasks that involve visual context. However, unlike humans who can reliably apply solution steps to similar problems with minor modifications, state-of-the-art VLMs such as GPT-4o often fail to maintain consistency across such variations, revealing limitations in their mathematical reasoning capabilities.

**DynaMATH** addresses this challenge by providing a **dynamic** visual math benchmark specifically designed to evaluate the **mathematical reasoning robustness** of VLMs. While existing vision-based math benchmarks assess VLMs' problem-solving abilities with static problem sets, they lack the ability to evaluate performance robustness under varying problem conditions.

DynaMATH bridges this gap by introducing a benchmark with 501 high-quality, multi-topic **seed** questions, each represented as a **Python program**. These programs enable automatic generation of a much larger set of **concrete** questions with diverse visual and textual variations, providing a comprehensive testbed for evaluating generalization abilities of VLMs.

<p align="center">
    <img src="assets/DynaMATH_demo.png" width="90%"> <br>
    Figure: Illustration of the dynamic benchmark generation process in DynaMATH.
</p>

We assessed the performance of 14 state-of-the-art VLMs using 5,010 generated concrete questions (10 variations per seed question). The results reveal that the **worst-case model accuracy**, defined as the percentage of correctly answered seed questions across all variations, is significantly lower than the average-case accuracy. Moreover, the analysis shows that model errors on certain variants are not merely due to random chance, but are consistent failures that indicate underlying robustness issues. The findings highlight the need to study the robustness of VLMs' reasoning capabilities. DynaMATH offers valuable insights for developing more reliable models for mathematical reasoning tasks.

## 📊 Benchmark Design

### Dataset Collection

Our benchmark collection consists of two phases: **Seed Question Collection** and **Program-based Question Generation**.

#### Seed Question Collection
- Seed questions were selectively curated from existing visual math datasets and publicly available resources.
- We collected:
  - **107 questions** from [MathVista](https://mathvista.github.io/), covering topics like analytic geometry and statistics.
  - **27 questions** from [MATH-V](https://mathvision-cuhk.github.io/), focused on arithmetic, puzzles, and solid geometry.
  - **45 questions** based on scientific figures.
  - **48 questions** on graph theory from the [MMMU](https://mmmu-benchmark.github.io/) dataset.
  - **236 questions** on advanced reasoning topics such as functions and geometry from publicly accessible resources.
  - **38 newly developed questions** covering linear algebra, set theory, and algorithmic flow.

- After eliminating overly complex questions unsuitable for programmatic generation, the final dataset comprises **501 seed questions**:
  - **45.3%** sourced from established visual math datasets.
  - **54.7%** newly collected or developed from public resources.


#### Program-based Question Generation
- Each seed question is transformed into a carefully designed Python program, enabling the generation of diverse concrete questions under randomly sampled conditions.
- **470 programs** include a plotting function for dynamic visual contexts, while **31 programs** use fixed images with randomized text elements.
-This programmatic approach enables the creation of **infinitely many** concrete benchmark questions, facilitating the evaluation of VLMs' reasoning robustness.

**Variant Types in DynaMath**:
1. **Numerical Value Variants**: Modifying numerical quantities to test arithmetic proficiency.
2. **Geometric Transformations**: Changing shapes, angles, and dimensions to assess spatial understanding.
3. **Function Type Variants**: Varying function types (e.g., linear, quadratic) to evaluate generalization.
4. **Color Variants**: Altering colors to test robustness against superficial visual changes.
5. **Symbolic Substitutions**: Modifying symbols to test adaptability to different mathematical representations.
6. **Graph Structure Variants**: Changing graph layouts to evaluate comprehension of relationships.
7. **Real-life Context Variants**: Modifying real-world scenarios (e.g., calendars, time-related problems) to test contextual understanding.

### Dataset Statistics
- **Mathematical Topics**: Covers nine topics including Solid Geometry (SG, 3.0%), Puzzle Tests (PT, 3.4%), Arithmetic (AR, 5.2%), Scientific Figures (SF, 9.0%), Graph Theory (GT, 9.6%), Algebra (AL, 10.2%), Plane Geometry (PG, 15.4%), Analytic Geometry (AG, 19.4%), and Statistics (ST, 25.0%). 
- **Difficulty Levels**: Questions range from elementary to undergraduate level, with a focus on high school (55.3%) and undergraduate (32.1%) levels.
- **Question Types**: Includes 35.5% multiple-choice questions and 64.7% free-form questions.

This diverse collection of variants and topics makes DynaMath a comprehensive benchmark for evaluating the flexibility, robustness, and accuracy of VLMs in solving mathematical problems.


## 🔍 Experiment Results

To evaluate the mathematical reasoning robustness of existing VLMs on DynaMath, we generate 10 [variants](./samples%20and%20result/10trials), resulting in a total of 5,010 questions to assess their performance.

### Average-case accuracy

The following table shows the Average-case accuracy of 14 models (three Closed-sourced Large Multimodal Models (LMMs) and 11 Vision Language Models (VLMs)) on DynaMath with 5,010 generated questions.


| Model                         | **ALL** | **PG**  | **SG**  | **AG**  | **AL**  | **PT**  | **GT**  | **ST**  | **SF**  | **AR**  | **EL**  | **HI**  | **UN**  |
|-------------------------------|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
| **Closed-sourced LLMs** |       |       |       |       |       |       |       |       |       |       |       |       |       |
| **Zero-shot GPT-4o**          |   59.2  |   53.1  |   50.0  |   57.5  |   78.0  |   37.1  |   57.5  |   63.8  |   54.2  |   53.5  |   61.4  |   56.9  |   34.6  |
| **Zero-shot Claude-3.5**      |   61.8  |   47.9  |   48.0  |   51.1  |   81.4  |   36.5  |   66.7  |   71.0  |   56.4  |   51.9  |   60.5  |   58.0  |   30.8  |
| **Zero-shot Gemini Pro 1.5**  |   56.2  |   50.4  |   41.3  |   57.7  |   69.4  |   21.8  |   57.3  |   61.6  |   48.9  |   45.0  |   61.4  |   54.1  |   34.8  |
| **3-shot GPT-4o**         | **61.9**| **56.1**| **55.3**| **54.5**| **82.2**|   35.3  |   62.5  |   64.6  |   57.8  |   57.7  | **65.7**|   57.5  |   33.0  |
| **3-shot Claude-3.5**     |   58.4  |   46.8  |   46.7  |   44.3  |   80.6  | **38.8**|   55.2  | **71.9**| **62.2**|   55.8  |   62.9  |   56.6  |   26.7  |
| **3-shot Gemini Pro 1.5** |   55.8  |   50.9  |   44.0  |   50.6  |   71.2  |   24.7  |   56.2  |   63.6  |   53.1  |   51.9  |   62.4  |   54.8  |   30.5  |
| **Open-sourced VLMs** |       |       |       |       |       |       |       |       |       |       |       |       |       |
| **Qwen2-VL-72B**              | **50.7**| **45.5**| **38.0**| **47.3**| **57.6**| **27.1**| **45.8**| **61.2**| **49.6**| **48.1**| **56.5**| **51.1**| **28.5**|
| **Qwen2-VL-7B**               |   39.4  |   37.1  |   33.3  |   38.2  |   37.8  |   10.0  |   41.5  |   48.1  |   37.8  |   34.2  |   45.7  |   38.8  |   23.0  |
| **InternVL2-76B**             |   49.6  |   42.3  |   40.7  |   42.1  |   63.3  |   15.9  |   49.6  |   62.6  |   46.0  |   43.1  |   53.2  |   49.2  |   25.3  |
| **InternVL2-40B**             |   37.6  |   30.9  |   28.0  |   33.5  |   35.5  |   14.7  |   37.7  |   51.1  |   37.3  |   32.3  |   47.3  |   35.8  |   20.2  |
| **InternVL2-26B**             |   39.8  |   36.8  |   29.3  |   36.9  |   41.0  |    9.4  |   42.5  |   50.5  |   37.6  |   31.5  |   45.7  |   38.0  |   22.2  |
| **InternVL2-8B**              |   30.1  |   26.4  |   21.3  |   28.4  |   34.1  |   10.0  |   31.5  |   35.8  |   29.6  |   29.6  |   39.8  |   27.7  |   17.1  |
| **Llama-3.2-90B**             |   37.4  |   35.6  |   34.0  |   34.8  |   32.9  |   13.5  |   29.2  |   46.8  |   32.4  |   21.5  |   36.0  |   35.7  |   21.0  |
| **Deepseek-VL-7B-chat**       |   20.6  |   17.3  |   15.3  |   26.5  |    8.8  |    1.8  |   32.3  |   23.8  |   19.3  |   12.7  |   24.3  |   18.7  |   16.0  |
| **Llava-v1.6-34B**            |   22.9  |   20.3  |   18.0  |   22.8  |   12.4  |    9.4  |   27.9  |   31.8  |   21.8  |   12.7  |   30.2  |   20.0  |   13.7  |
| **Llava-v1.6-vicuna-13B**     |   15.7  |   11.4  |    5.3  |   21.8  |    8.4  |    4.1  |   26.7  |   17.7  |   13.3  |    5.8  |   18.6  |   12.5  |   13.1  |
| **Llava-v1.5-7B**             |   13.3  |    8.6  |    6.7  |   17.1  |    7.6  |    4.1  |   25.6  |   14.6  |   12.2  |    7.3  |   13.5  |   11.0  |   10.3  |
| **Human** |       |       |       |       |       |       |       |       |       |       |       |       |       |
| **Human performance**         | **72.9**| **75.3**| **40.0**| **79.4**| **80.4**| **70.6**| **64.6**| **73.6**| **73.3**| **57.7**| **73.0**| **73.3**| **71.4**|



- **Closed-Source Models:**
  - Average performance of GPT-4o, Claude-3.5, and Gemini Pro 1.5 hovers around 60%, with Claude-3.5 achieving the highest zero-shot average accuracy at 61.8%.
  - There remains an 11.1% gap between the highest closed-source model (Claude-3.5) and human performance (72.9%), indicating room for improvement in VLMs' reasoning abilities.
  - In the 3-shot CoT setting, there is no consistent improvement:
    - 3-shot CoT GPT-4o improves from 59.2% to 61.9%.
    - However, 3-shot CoT Claude-3.5 and 3-shot CoT Gemini Pro 1.5 see performance declines.

- **Open-Source Models:**
  - Generally underperform compared to closed-source models, but recent advancements have narrowed the gap.
  - Larger open-source models such as Qwen2-VL-72B and InternVL2-76B are showing promise, with scaling trends indicating better performance as parameter sizes increase.
  - For example:
    - Qwen2-VL's accuracy rises from 39.4% (7B parameters) to 50.7% (72B parameters).
    - InternVL2's accuracy increases from 30.1% (8B parameters) to 49.6% (76B parameters).


### Worst-case accuracy

The following table shows the Worst-case accuracy of 14 models (three Closed-sourced Large Multimodal Models (LMMs) and 11 Vision Language Models (VLMs)) on DynaMath with 5,010 generated questions.


| **Model**                    | **ALL** | **PG** | **SG** | **AG** | **AL** | **PT** | **GT** | **ST** | **SF** | **AR** | **EL** | **HI** | **UN** |
|------------------------------|:-------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| **Closed-sourced LMMs** |       |       |       |       |       |       |       |       |       |       |       |       |       |
| **Zero-shot GPT-4o**         |  27.9   |  26.0  |  26.7  |  23.7  |  51.0  |  5.9   |  14.6  |  32.0  |  17.8  |  38.5  |  30.2  |  27.4  |  26.7  |
| **Zero-shot Claude-3.5**     |  27.7   |  23.4  |  26.7  |  12.4  | **52.9** |  17.6  |  16.7  |  35.2  | **31.1** |  34.6  |  36.5  |  27.1  |  25.5  |
| **Zero-shot Gemini Pro 1.5** |  23.2   |  26.0  |  20.0  |  18.6  |  31.4  |  5.9   |  18.8  |  24.4  |  24.4  |  26.9  | **39.7**|  22.4  |  18.0  |
| **3-shot GPT-4o**        | **31.7**| **31.2**| **33.3**| **25.8**|  51.0  | **11.8**| **22.9**| **34.4**|  24.4  | **46.2**| **39.7**| **30.3**| **31.1**|
| **3-shot Claude-3.5**    |  25.1   |  20.8  |  26.7  |  10.3  |  49.0  |  17.6  |  12.5  |  32.8  |  28.9  |  30.8  |  38.1  |  23.5  |  23.0  |
| **3-shot Gemini Pro 1.5**|  20.8   |  24.7  |  20.0  |  11.3  |  27.5  |  0.0   |  18.8  |  22.2  |  22.2  |  26.9  |  33.3  |  20.2  |  16.8  |
| **Open-sourced VLMs** |       |       |       |       |       |       |       |       |       |       |       |       |       |
| **Qwen2-VL-72B**             | **18.4**| **20.8**| **13.3**| **8.2** |  21.6  |  0.0   | **10.4**| **28.0**| **17.8**| **26.9**| **33.3**| **18.1**| **13.0**|
| **Qwen2-VL-7B**              |   6.6   |  10.4  |  0.0   |  6.2   |  3.9   |  0.0   |  2.1   |  11.2  |  2.2   |  3.8   |  17.5  |  6.1   |  3.1   |
| **InternVL2-76B**            |  15.4   |  13.0  | **20.0**|  7.2   | **29.4**|  0.0   | **10.4**|  21.6  |  15.6  |  11.5  |  23.8  |  14.8  | **13.0**|
| **InternVL2-40B**            |   6.0   |   9.1  |  13.3  |  3.1   |  3.9   |  0.0   |  2.1   |  8.9   |  8.9   |  3.8   |  15.9  |  5.4   |  3.1   |
| **InternVL2-26B**            |   8.6   |  11.7  |  0.0   |  4.1   |  7.8   |  0.0   |  8.3   |  12.0  |  13.3  |  3.8   |  19.0  |  7.6   |  6.2   |
| **InternVL2-8B**             |   3.4   |   6.5  |  0.0   |  1.0   |  5.9   |  0.0   |  2.1   |  4.0   |  2.2   |  3.0   |  9.5   |  3.2   |  1.2   |
| **Llama-3.2-90B**            |   4.6   |   1.3  |  0.0   |  2.1   |  13.3  |  0.0   |  5.9   |  2.2   |  0.0   |  0.0   |  7.9   |  4.3   |  1.9   |
| **Deepseek-VL-7B-chat**      |   2.0   |   3.0  |  0.0   |  1.6   |  0.0   |  0.0   |  0.0   |  3.8   |  0.0   |  0.0   |  6.3   |  1.1   |  0.6   |
| **Llava-v1.6-34B**           |   1.8   |   3.9  |  0.0   |  0.0   |  2.0   |  0.0   |  4.2   |  0.0   |  0.0   |  0.0   |  7.9   |  1.2   |  0.6   |
| **Llava-v1.6-vicuna-13B**    |   0.2   |   0.0  |  0.0   |  0.0   |  0.0   |  0.0   |  0.0   |  0.0   |  0.0   |  0.0   |  1.6   |  0.0   |  0.0   |
| **Llava-v1.5-7B**            |   0.2   |   0.0  |  0.0   |  0.0   |  0.0   |  0.0   |  0.0  |  0.0   |  0.0   |  0.0   |  2.1   |  0.0   |  0.6   |


- **Performance Decline in Variant Handling:**
  - All models experience significant declines in worst-case accuracy across 10 problem variants.
  - GPT-4o has the highest zero-shot worst-case score at only 27.7%, increasing marginally to 31.7% in the 3-shot CoT setting.
  - Open-source models struggle even more with worst-case scenarios:
    - Qwen2-VL-72B, the best-performing open-source model, achieves only 18.4%.
    - Smaller models like Llava-v1.6-vicuna-13B achieve a score as low as 0.2%.

- **Insights and Challenges:**
  - These results highlight the limited robustness of current VLMs in handling problem variations.
  - The findings underscore the need for the research community to focus on improving model consistency and robustness under varying contexts and visual changes.



## 📖 Dataset Usage

### Generating a Version of DynaMath

Follow these steps to generate a version of the DynaMath dataset:

#### Step 1: Build the Docker Image

First, use the provided `Dockerfile` to create a Docker image for the environment:

```bash
docker build -t dynamath .
```

#### Step 2: Run the Docker Container

Next, run the container interactively based on the created image, ensuring you mount the appropriate directories:

```bash
docker run -it -v /home/user/DynaMATH:/app dynamath bash
```

#### Step 3: Generate Variant Questions

Once inside the container, navigate to the `dataset_generator` directory and generate the question variants by running:

```bash
cd dataset_generator
xvfb-run -s "-screen 0 640x480x24" python generate_json.py 1 501
```

This will generate a batch of questions starting from index 1 to 501.

> **Note:** The `generate_json.py` script takes four arguments:
> 1. Starting index
> 2. Number of questions to generate from the starting index
> 3. Default random seed
> 4. Default NumPy seed

