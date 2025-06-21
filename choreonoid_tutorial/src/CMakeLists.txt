choreonoid_add_simple_controller(StandController StandController.cpp)

choreonoid_add_simple_controller(ROSChoreonoidBridgeController ROSChoreonoidBridgeController.cpp)
target_link_libraries(ROSChoreonoidBridgeController ${roscpp_LIBRARIES})


# inference
set(Torch_DIR "$ENV{HOME}/genesis_ws/libtorch/share/cmake/Torch")
find_package(Torch REQUIRED)
choreonoid_add_simple_controller(InferenceController InferenceController.cpp)
target_link_libraries(InferenceController ${CHOREONOID_BASE_LIBRARIES} "${TORCH_LIBRARIES}")
set_property(TARGET InferenceController PROPERTY CXX_STANDARD 17)
