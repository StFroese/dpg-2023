from argparse import ArgumentParser
import matplotlib.pyplot as plt
from ctapipe.io import EventSource
from ctapipe.reco import HillasReconstructor, Model3DGeometryReconstructor
from ctapipe.image import ImageProcessor

parser = ArgumentParser()
parser.add_argument('outfile')
parser.add_argument('datadir')
args = parser.parse_args()

name, suffix = args.outfile.split('.')
basename, _ = name.split('_')

source = EventSource(args.datadir + '/gamma_20deg_180deg_run3___cta-prod6-paranal-2147m-Paranal-dark.dl2.h5', max_events=10)

events = list(source)

image_processor = ImageProcessor(source.subarray)
hillas_reco = HillasReconstructor(source.subarray)
model3d = Model3DGeometryReconstructor(source.subarray)
for idx, event in enumerate(events):
    image_processor(event)
    hillas_reco(event)
    model3d(event)
    model3d.peek(event, show=False)
    plt.savefig(f'{basename}_{idx}.{suffix}')
    plt.close()
