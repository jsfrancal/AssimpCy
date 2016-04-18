from __future__ import print_function
import setpath

from timeit import Timer

from assimpcy import aiImportFile, aiPostProcessSteps as pp

from os import path as pt

home = pt.dirname(__file__)

path = './models/cil/cil.x'
# path = '/models/dragon.obj'
# path = '/models/shadow room/lightmapped.x'
# path = '/models/sponza/sponza.3DS'

scene = None


def doImport():
    global path, scene
    flags = pp.aiProcess_JoinIdenticalVertices | pp.aiProcess_Triangulate | pp.aiProcess_CalcTangentSpace | \
            pp.aiProcess_OptimizeGraph | pp.aiProcess_OptimizeMeshes | \
            pp.aiProcess_FixInfacingNormals | pp.aiProcess_GenUVCoords | \
            pp.aiProcess_LimitBoneWeights | pp.aiProcess_SortByPType | pp.aiProcess_RemoveRedundantMaterials

    scene = aiImportFile(pt.join(home, path), flags)


def main():
    global scene
    print('Reading \'{}\':'.format(path))
    t = Timer(doImport)
    secs = t.timeit(1)
    print('\tHas {} meshes, {} textures, {} materials, {} animations.'.format(scene.mNumMeshes,
                                                                              scene.mNumTextures,
                                                                              scene.mNumMaterials,
                                                                              scene.mNumAnimations))

    # Check mesh.Has* before extracting corresponding mesh.m* (Vertices, Normals, etc)
    if scene.HasMeshes and scene.mMeshes[0].HasPositions:
        v = int(scene.mMeshes[0].mNumVertices / 2)
        print('\tVertex {} = {}'.format(v, scene.mMeshes[0].mVertices[v]))
        # print()
        # print(scene.mRootNode.mChildren[0].mTransformation)

    print('Took {:0.4f} seconds.'.format(secs))


if __name__ == '__main__':
    main()
