import json
from api_package.kingjimin.kingjimin import DeviceFarmGateway

if __name__ == "__main__":
    # initialize
    apiclass = DeviceFarmGateway("gateway.devicefarm-dev.netspresso.ai", "80")

    # unittest.main()

    # get all nodes(res is list)
    # res = apiclass.get_all_nodes()

    # get a node info
    # node, error = apiclass.get_node("8fefe378-ff5a-11eb-9305-dca6328392f4")
    # res, error = apiclass.get_node(node)

    # get all tasks of a node
    # res, error = apiclass.get_tasks_of_node("938b4106-3d3c-11ec-9388-b827eba9d011")
    # res, error = apiclass.get_tasks_of_node(node)

    # get a task 
    # task, error = apiclass.get_task("907e77ff-656d-4039-a632-797f55817894")
    # res, error = apiclass.get_task(task)

    # get all models info
    # res = apiclass.get_all_models()

    # get model
    # model, error = apiclass.get_model("14bbaaac-8e44-43fb-91d0-3b09b2664654")
    # res, error = apiclass.get_model(model)

    # get available nodes
    # nodes, error = apiclass.get_available_nodes("59c3714e-1c6a-40b7-9404-a045c570d1df")
    # nodes, error = apiclass.get_available_nodes(model)
    # [print(res[i].uuid) for i in range(0, len(res))]

    # delete model
    # model, error = apiclass.delete_model("09940e28-2a33-4a21-8ebf-6272a6b14cc5")
    # res, error = apiclass.delete_model(model)

    # delete only model
    # model, error = apiclass.delete_only_model_file("5f0a1c87-394a-4bb1-8f6a-b36685249a7b")
    # res, error = apiclass.delete_only_model_file(model)

    # upload model
    # res, error = apiclass.upload_model('/hdd1/home/jmlee/fp16.tflite', 'tflite')

    # download model
    # res, error = apiclass.download_model_file("83b4008a-d1c7-4b51-8417-ef97466d1ff9")
    # res, error = apiclass.download_model_file(model)
    # with open(f"./api.tflite", "wb") as f:
    #     f.write(res.content)

    # start benchmark(nodes is list)
    # benchmark_args= {
    #     "use_gpu": True,
    #     "use_xnnpack": True,
    #     "num_runs": 3,
    #     "num_threads": 4,
    #     "additional_options": "--allow_fp16",
    #     # "callback_url": "http://192.168.1.202:8000/get/"
    #     }
    # result = apiclass.start_benchmark("59c3714e-1c6a-40b7-9404-a045c570d1df", "-", benchmark_args)
    # result = apiclass.start_benchmark(model, [nodes[0]], benchmark_args, False)
    # print(result)

    # get all benchmarks on a model
    # benchmarks, error = apiclass.get_all_benchmarks_of_model("c4af7556-24e4-4c51-8576-a3ff4b596ab7")
    # res, error = apiclass.get_all_benchmarks_of_model(model)

    # get benchmark on a model
    # benchmark, error = apiclass.get_benchmark_of_model(model, "02e533ae-7e04-4eec-8699-40d3b34060ff")
    # res, error = apiclass.get_benchmark_of_model(model, "b9032629-c7ab-4904-8bab-4019cf225ae3")

    # delete benchmark
    # benchmark, error = apiclass.delete_benchmark("f380b34b-8e5c-454f-b57f-d20cc73257c6", "c29c55c2-a9e2-49aa-b938-9c00a8a1dc18")
    # res, error = apiclass.delete_benchmark(model, "b9032629-c7ab-4904-8bab-4019cf225ae3")

    # res = apiclass.wrapping_callback(data)
    # print(res.uuid)

    # parse and print res
    # content = json.loads(res.content.decode('utf-8'))
    # print(content)