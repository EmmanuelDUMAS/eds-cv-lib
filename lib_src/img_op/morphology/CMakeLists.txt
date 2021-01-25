# CMakeList.txt
# lib_src/img_op/morphology

add_subdirectory(dilate)

# tips for move from local scope to parent scope
set(eds_cv_lib_sources "${eds_cv_lib_sources}" PARENT_SCOPE)

# message(STATUS "eds_cv_lib_sources " ${eds_cv_lib_sources})

# end of file
