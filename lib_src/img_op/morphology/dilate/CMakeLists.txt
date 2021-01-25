# CMakeList.txt
# lib_src/img_op/morphology/dilate

list(APPEND eds_cv_lib_sources 
    ${CMAKE_CURRENT_SOURCE_DIR}/ecv_dilate_3x3_u8.c
    ${CMAKE_CURRENT_SOURCE_DIR}/ecv_dilate_3x3_u16.c
)

# tips for move from local scope to parent scope
set(eds_cv_lib_sources "${eds_cv_lib_sources}" PARENT_SCOPE)

# message(STATUS "eds_cv_lib_sources " ${eds_cv_lib_sources})

# end of file
