# Devicefarm API Package

## Introduction

Devicefarm API Package는 devicefarm에 있는 endpoint를 코드로 쉽게 사용할 수 있도록 만든 패키지입니다. 이 API Package에서는 Devicefarm에 특정 요청을 날린 후 정보를 받아와 Dataclass로 Wrapping하여 Return이 되기 때문에, Wrapping 전 정보를 확인하고 싶으시거나 API Package를 사용하지 않고 Devicefarm API를 사용하고 싶으시다면 아래 링크로 들어가서 Devicefarm API Document를 확인해주시기 바랍니다.

- https://github.com/nota-github/device_farm_gateway/blob/main/readme_files/device_farm_gateway_api.html



## How to use

터미널에 아래 명령어를 입력하여 패키지를 다운받으면 바로 사용하실 수 있습니다.

```bash
pip3 install kingjimin -U
```



## API Information

- devicefarm_api_package/api_package/kingjimin/data.py : Dataclass 구조를 확인할 수 있습니다.
- devicefarm_api_package/api_package/kingjimin/kingjimin.py : 함수 알고리즘 및 함수별 정보를 확인할 수 있습니다.
- api_test.py : 함수별 사용 예제를 볼 수 있습니다.



#### 1. get_all_nodes()

- 설명 : Devicefarm에 등록된 모든 노드 정보들을 가져온다.

- 반환
  - 성공 : Node Instance들로 이루어진 list, None
  - 실패 : None, Error



#### 2. get_node(node_uuid: str)

- 설명 : node_uuid 값과 같은 uuid를 가진 노드 정보를 가져온다.
- 입력
  - node_uuid: 정보를 받아오고 싶은 노드의 uuid
- 반환
  - 성공 : Node, None
  - 실패 : None, Error



#### 3. get_tasks_of_node(node_uuid: str)

- 설명 : node_uuid 값과 같은 uuid를 가진 노드의 task 정보들을 가져온다.
- 입력
  - node_uuid: Task 정보를 받아오고 싶은 노드의 uuid
- 반환
  - 성공 : Task Instance들로 이루어진 list, None
  - 실패 : None, Error



#### 3-1. get_tasks_of_node(node: Node)

설명 및 반환은 3번과 동일합니다.

- 입력
  - node: Task 정보를 받아오고 싶은 노드의 Node Dataclass



#### 4. get_task(task_uuid: str)

- 설명 : task_uuid 값과 같은 uuid를 가진 Task 정보를 가져온다.
- 입력
  - task_uuid: 정보를 받아오고 싶은 Task의 uuid
- 반환
  - 성공 : Task, None
  - 실패 : None, Error



#### 5. get_all_models()

- 설명 : Devicefarm에 등록된 모든 Model 정보들을 가져온다.
- 반환
  - 성공 : Model Instance들로 이루어진 list, None
  - 실패 : None, Error



#### 6. get_model(model_uuid: str)

- 설명 : model_uuid 값과 같은 uuid를 가진 Model 정보를 가져온다.
- 입력
  - model_uuid: 정보를 받아오고 싶은 Model의 uuid
- 반환
  - 성공 : Model, None
  - 실패 : None, Error



#### 7. get_available_nodes(model_uuid: str)

- 설명 : model_uuid 값과 같은 uuid를 가진 Model 정보를 가져온다.
- 입력
  - model_uuid: 정보를 받아오고 싶은 Model의 uuid
- 반환
  - 성공 : Model, None
  - 실패 : None, Error



#### 7-1. get_available_nodes(model: Model)

설명 및 반환은 7번과 동일합니다.

- 입력
  - model: 정보를 받아오고 싶은 모델의 Model Dataclass



#### 8. delete_model(model_uuid: str)

- 설명 : model_uuid에 해당하는 Model과 그 모델의 모든 Benchmark를 삭제한다.
- 입력
  - model_uuid: 삭제할 Model의 uuid
- 반환
  - 성공 : Model, None
  - 실패 : None, Error



#### 8-1. delete_model(model: Model)

설명 및 반환은 8번과 동일합니다.

- 입력
  - model: 삭제할 모델의 Model Dataclass



#### 9. delete_only_model_file(model_uuid: str)

- 설명 : model_uuid에 해당하는 Model을 모델 파일만 삭제한다.
- 입력
  - model_uuid: 삭제할 Model의 uuid
- 반환
  - 성공 : Model, None
  - 실패 : None, Error



#### 9-1. delete_only_model_file(model: Model)

설명 및 반환은 9번과 동일합니다.

- 입력
  - model: 삭제할 모델의 Model Dataclass



#### 10. upload_model(model_path: str, model_type: str)

- 설명 : 모델 파일을 업로드하고 Gateway에서 생성된 Model 정보를 돌려받는다.
- 입력
  - model_path: 업로드할 모델의 local path
  - model_type: 업로드할 모델의 type (ex: onnx, onnx-trt, tflite)
- 반환
  - 성공 : Model, None
  - 실패 : None, Error



#### 11. download_model_file(model_uuid: str)

- 설명 : model_uuid에 해당하는 Model의 파일을 다운로드한다.
- 입력
  - model_uuid: 다운받고 싶은 모델의 uuid
- 반환
  - 성공 : byte 형태의 모델, None
  - 실패 : None, Error



#### 11-1. download_model_file(model: Model)

설명 및 반환은 11번과 동일합니다.

- 입력
  - model: 다운받고 싶은 모델의 Model Dataclass



#### 12. start_benchmark(model_uuid: str, node_list: list, benchmark_args: dict, verbose: bool)

- 설명 : benchmark_args에 있는 옵션과 함께 model_uuid에 해당하는 모델을 node_list에 있는 노드에서 벤치마크를 실행한다.
- 입력
  - model_uuid: 벤치마크를 돌릴 모델의 uuid
  - node_list: 벤치마크를 돌릴 노드의 uuid(*list*)
  - benchmark_args: 벤치마크 옵션(ex. use_gpu, use_xnnpack)
  - verbose(optional): 벤치마크 argument를 콘솔에 출력할지에 대한 bool 값(default = False)
- 반환
  - 성공 : Benchmark, Model, Node Instance들로 이루어진 list, None
  - 실패 : None, None, None, Error



#### 12-1. start_benchmark(model: Model, node_list: list, benchmark_args: dict, verbose: bool)

설명 및 반환은 12번과 동일합니다.

- 입력
  - model: 벤치마크를 돌릴 모델의 Model Dataclass
  - node_list: 벤치마크를 돌릴 노드의 uuid(*list*)
  - benchmark_args: 벤치마크 옵션(ex. use_gpu, use_xnnpack)
  - verbose(optional): 벤치마크 argument를 콘솔에 출력할지에 대한 bool 값(default = False)



#### 13. get_all_benchmarks_of_model(model_uuid: str)

- 설명 : model_uuid에 해당하는 Model의 벤치마크 정보들을 가져온다.
- 입력
  - model_uuid: Benchmark 정보들을 가져올 Model의 uuid
- 반환
  - 성공 : Benchmark Instance들로 이루어진 list, None
  - 실패 : None, Error



#### 13-1. get_all_benchmarks_of_model(model: Model)

설명 및 반환은 13번과 동일합니다.

- 입력
  - model: Benchmark 정보들을 가져올 모델의 Model Dataclass



#### 14. get_benchmark_of_model(model_uuid: str, bench_uuid: str)

- 설명 : model_uuid에 해당하는 Model에서 bench_uuid에 해당하는 벤치마크 정보를 가져온다.
- 입력
  - model_uuid: Benchmark 정보들을 가져올 Model의 uuid
  - bench_uuid: 가져올 Benchmark의 uuid
- 반환
  - 성공 : Benchmark, None
  - 실패 : None, Error



#### 14-1. get_benchmark_of_model(model: Model, bench_uuid: str)

설명 및 반환은 14번과 동일합니다.

- 입력
  - model: Benchmark 정보들을 가져올 모델의 Model Dataclass
  - bench_uuid: 가져올 Benchmark의 uuid



#### 15. delete_benchmark(model_uuid: str, bench_uuid: str)

- 설명 : model_uuid에 해당하는 Model에서 bench_uuid에 해당하는 벤치마크를 삭제한다.
- 입력
  - model_uuid: 삭제할 Benchmark가 등록된 Model의 uuid
  - bench_uuid: 삭제할 Benchmark의 uuid
- 반환
  - 성공 : Benchmark, None
  - 실패 : None, Error



#### 15-1. delete_benchmark(model: Model, bench_uuid: str)

설명 및 반환은 15번과 동일합니다.

- 입력
  - model: 삭제할 Benchmark가 등록된 모델의 Model Dataclass
  - bench_uuid: 삭제할 Benchmark의 uuid



#### 15-2. delete_benchmark(bench: Benchmark)

설명 및 반환은 15번과 동일합니다.

- 입력
  - bench: 삭제할 벤치마크의 Benchmark Dataclass



#### 16. wrapping_callback(callback_data)

- 설명 : Benchmark status update될 때 받아온 callback_data를 Benchmark Instance로 반환한다.
- 입력
  - callback_data: Benchmark Instance로 변환할 callback data
- 반환
  - 성공 : Benchmark, None
  - 실패 : None, Error