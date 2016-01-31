#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.24-aodv-optimized', 'build/src/bridge/examples/ns3.24-csma-bridge-optimized', 'build/src/bridge/examples/ns3.24-csma-bridge-one-hop-optimized', 'build/src/buildings/examples/ns3.24-buildings-pathloss-profiler-optimized', 'build/src/config-store/examples/ns3.24-config-store-save-optimized', 'build/src/core/examples/ns3.24-main-callback-optimized', 'build/src/core/examples/ns3.24-sample-simulator-optimized', 'build/src/core/examples/ns3.24-main-ptr-optimized', 'build/src/core/examples/ns3.24-main-random-variable-optimized', 'build/src/core/examples/ns3.24-main-random-variable-stream-optimized', 'build/src/core/examples/ns3.24-sample-random-variable-optimized', 'build/src/core/examples/ns3.24-sample-random-variable-stream-optimized', 'build/src/core/examples/ns3.24-command-line-example-optimized', 'build/src/core/examples/ns3.24-hash-example-optimized', 'build/src/core/examples/ns3.24-main-test-sync-optimized', 'build/src/csma/examples/ns3.24-csma-one-subnet-optimized', 'build/src/csma/examples/ns3.24-csma-broadcast-optimized', 'build/src/csma/examples/ns3.24-csma-packet-socket-optimized', 'build/src/csma/examples/ns3.24-csma-multicast-optimized', 'build/src/csma/examples/ns3.24-csma-raw-ip-socket-optimized', 'build/src/csma/examples/ns3.24-csma-ping-optimized', 'build/src/csma-layout/examples/ns3.24-csma-star-optimized', 'build/src/dsdv/examples/ns3.24-dsdv-manet-optimized', 'build/src/dsr/examples/ns3.24-dsr-optimized', 'build/src/energy/examples/ns3.24-li-ion-energy-source-optimized', 'build/src/energy/examples/ns3.24-rv-battery-model-test-optimized', 'build/src/energy/examples/ns3.24-basic-energy-model-test-optimized', 'build/src/fd-net-device/examples/ns3.24-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.24-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.24-realtime-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.24-realtime-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.24-fd-emu-ping-optimized', 'build/src/fd-net-device/examples/ns3.24-fd-emu-udp-echo-optimized', 'build/src/fd-net-device/examples/ns3.24-fd-emu-onoff-optimized', 'build/src/fd-net-device/examples/ns3.24-fd-tap-ping-optimized', 'build/src/fd-net-device/examples/ns3.24-fd-tap-ping6-optimized', 'build/src/internet/examples/ns3.24-main-simple-optimized', 'build/src/internet/examples/ns3.24-codel-vs-droptail-basic-test-optimized', 'build/src/internet/examples/ns3.24-codel-vs-droptail-asymmetric-optimized', 'build/src/lr-wpan/examples/ns3.24-lr-wpan-packet-print-optimized', 'build/src/lr-wpan/examples/ns3.24-lr-wpan-phy-test-optimized', 'build/src/lr-wpan/examples/ns3.24-lr-wpan-data-optimized', 'build/src/lr-wpan/examples/ns3.24-lr-wpan-error-model-plot-optimized', 'build/src/lr-wpan/examples/ns3.24-lr-wpan-error-distance-plot-optimized', 'build/src/lte/examples/ns3.24-lena-cqi-threshold-optimized', 'build/src/lte/examples/ns3.24-lena-dual-stripe-optimized', 'build/src/lte/examples/ns3.24-lena-fading-optimized', 'build/src/lte/examples/ns3.24-lena-intercell-interference-optimized', 'build/src/lte/examples/ns3.24-lena-pathloss-traces-optimized', 'build/src/lte/examples/ns3.24-lena-profiling-optimized', 'build/src/lte/examples/ns3.24-lena-rem-optimized', 'build/src/lte/examples/ns3.24-lena-rem-sector-antenna-optimized', 'build/src/lte/examples/ns3.24-lena-rlc-traces-optimized', 'build/src/lte/examples/ns3.24-lena-simple-optimized', 'build/src/lte/examples/ns3.24-lena-simple-epc-optimized', 'build/src/lte/examples/ns3.24-lena-deactivate-bearer-optimized', 'build/src/lte/examples/ns3.24-lena-x2-handover-optimized', 'build/src/lte/examples/ns3.24-lena-x2-handover-measures-optimized', 'build/src/lte/examples/ns3.24-lena-frequency-reuse-optimized', 'build/src/lte/examples/ns3.24-lena-distributed-ffr-optimized', 'build/src/lte/examples/ns3.24-lena-uplink-power-control-optimized', 'build/src/mesh/examples/ns3.24-mesh-optimized', 'build/src/mobility/examples/ns3.24-main-grid-topology-optimized', 'build/src/mobility/examples/ns3.24-main-random-topology-optimized', 'build/src/mobility/examples/ns3.24-main-random-walk-optimized', 'build/src/mobility/examples/ns3.24-mobility-trace-example-optimized', 'build/src/mobility/examples/ns3.24-ns2-mobility-trace-optimized', 'build/src/mobility/examples/ns3.24-bonnmotion-ns2-example-optimized', 'build/src/mpi/examples/ns3.24-simple-distributed-optimized', 'build/src/mpi/examples/ns3.24-third-distributed-optimized', 'build/src/mpi/examples/ns3.24-nms-p2p-nix-distributed-optimized', 'build/src/mpi/examples/ns3.24-simple-distributed-empty-node-optimized', 'build/src/netanim/examples/ns3.24-dumbbell-animation-optimized', 'build/src/netanim/examples/ns3.24-grid-animation-optimized', 'build/src/netanim/examples/ns3.24-star-animation-optimized', 'build/src/netanim/examples/ns3.24-wireless-animation-optimized', 'build/src/netanim/examples/ns3.24-uan-animation-optimized', 'build/src/netanim/examples/ns3.24-dynamic_linknode-optimized', 'build/src/netanim/examples/ns3.24-resources_demo-optimized', 'build/src/network/examples/ns3.24-main-packet-header-optimized', 'build/src/network/examples/ns3.24-main-packet-tag-optimized', 'build/src/network/examples/ns3.24-red-tests-optimized', 'build/src/network/examples/ns3.24-droptail_vs_red-optimized', 'build/src/network/examples/ns3.24-packet-socket-apps-optimized', 'build/src/nix-vector-routing/examples/ns3.24-nix-simple-optimized', 'build/src/nix-vector-routing/examples/ns3.24-nms-p2p-nix-optimized', 'build/src/olsr/examples/ns3.24-simple-point-to-point-olsr-optimized', 'build/src/olsr/examples/ns3.24-olsr-hna-optimized', 'build/src/point-to-point/examples/ns3.24-main-attribute-value-optimized', 'build/src/propagation/examples/ns3.24-main-propagation-loss-optimized', 'build/src/propagation/examples/ns3.24-jakes-propagation-model-example-optimized', 'build/src/sixlowpan/examples/ns3.24-example-sixlowpan-optimized', 'build/src/sixlowpan/examples/ns3.24-example-ping-lr-wpan-optimized', 'build/src/spectrum/examples/ns3.24-adhoc-aloha-ideal-phy-optimized', 'build/src/spectrum/examples/ns3.24-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-optimized', 'build/src/spectrum/examples/ns3.24-adhoc-aloha-ideal-phy-with-microwave-oven-optimized', 'build/src/spectrum/examples/ns3.24-tv-trans-example-optimized', 'build/src/spectrum/examples/ns3.24-tv-trans-regional-example-optimized', 'build/src/stats/examples/ns3.24-gnuplot-example-optimized', 'build/src/stats/examples/ns3.24-double-probe-example-optimized', 'build/src/stats/examples/ns3.24-time-probe-example-optimized', 'build/src/stats/examples/ns3.24-gnuplot-aggregator-example-optimized', 'build/src/stats/examples/ns3.24-gnuplot-helper-example-optimized', 'build/src/stats/examples/ns3.24-file-aggregator-example-optimized', 'build/src/stats/examples/ns3.24-file-helper-example-optimized', 'build/src/tap-bridge/examples/ns3.24-tap-csma-optimized', 'build/src/tap-bridge/examples/ns3.24-tap-csma-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.24-tap-wifi-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.24-tap-wifi-dumbbell-optimized', 'build/src/topology-read/examples/ns3.24-topology-read-optimized', 'build/src/uan/examples/ns3.24-uan-cw-example-optimized', 'build/src/uan/examples/ns3.24-uan-rc-example-optimized', 'build/src/virtual-net-device/examples/ns3.24-virtual-net-device-optimized', 'build/src/wave/examples/ns3.24-wave-simple-80211p-optimized', 'build/src/wave/examples/ns3.24-wave-simple-device-optimized', 'build/src/wave/examples/ns3.24-vanet-routing-compare-optimized', 'build/src/wifi/examples/ns3.24-wifi-phy-test-optimized', 'build/src/wifi/examples/ns3.24-test-interference-helper-optimized', 'build/src/wimax/examples/ns3.24-wimax-ipv4-optimized', 'build/src/wimax/examples/ns3.24-wimax-multicast-optimized', 'build/src/wimax/examples/ns3.24-wimax-simple-optimized', 'build/examples/socket/ns3.24-socket-bound-static-routing-optimized', 'build/examples/socket/ns3.24-socket-bound-tcp-static-routing-optimized', 'build/examples/socket/ns3.24-socket-options-ipv4-optimized', 'build/examples/socket/ns3.24-socket-options-ipv6-optimized', 'build/examples/routing/ns3.24-dynamic-global-routing-optimized', 'build/examples/routing/ns3.24-static-routing-slash32-optimized', 'build/examples/routing/ns3.24-global-routing-slash32-optimized', 'build/examples/routing/ns3.24-global-injection-slash32-optimized', 'build/examples/routing/ns3.24-simple-global-routing-optimized', 'build/examples/routing/ns3.24-simple-alternate-routing-optimized', 'build/examples/routing/ns3.24-mixed-global-routing-optimized', 'build/examples/routing/ns3.24-simple-routing-ping6-optimized', 'build/examples/routing/ns3.24-manet-routing-compare-optimized', 'build/examples/routing/ns3.24-ripng-simple-network-optimized', 'build/examples/naming/ns3.24-object-names-optimized', 'build/examples/matrix-topology/ns3.24-matrix-topology-optimized', 'build/examples/tcp/ns3.24-tcp-large-transfer-optimized', 'build/examples/tcp/ns3.24-tcp-nsc-lfn-optimized', 'build/examples/tcp/ns3.24-tcp-nsc-zoo-optimized', 'build/examples/tcp/ns3.24-tcp-star-server-optimized', 'build/examples/tcp/ns3.24-star-optimized', 'build/examples/tcp/ns3.24-tcp-bulk-send-optimized', 'build/examples/tcp/ns3.24-tcp-nsc-comparison-optimized', 'build/examples/tcp/ns3.24-tcp-variants-comparison-optimized', 'build/examples/realtime/ns3.24-realtime-udp-echo-optimized', 'build/examples/wireless/ns3.24-mixed-wireless-optimized', 'build/examples/wireless/ns3.24-wifi-adhoc-optimized', 'build/examples/wireless/ns3.24-wifi-clear-channel-cmu-optimized', 'build/examples/wireless/ns3.24-wifi-ap-optimized', 'build/examples/wireless/ns3.24-wifi-wired-bridging-optimized', 'build/examples/wireless/ns3.24-simple-msdu-aggregation-optimized', 'build/examples/wireless/ns3.24-multirate-optimized', 'build/examples/wireless/ns3.24-wifi-simple-adhoc-optimized', 'build/examples/wireless/ns3.24-wifi-simple-adhoc-grid-optimized', 'build/examples/wireless/ns3.24-wifi-simple-infra-optimized', 'build/examples/wireless/ns3.24-wifi-simple-interference-optimized', 'build/examples/wireless/ns3.24-wifi-blockack-optimized', 'build/examples/wireless/ns3.24-ofdm-validation-optimized', 'build/examples/wireless/ns3.24-ofdm-ht-validation-optimized', 'build/examples/wireless/ns3.24-ofdm-vht-validation-optimized', 'build/examples/wireless/ns3.24-wifi-hidden-terminal-optimized', 'build/examples/wireless/ns3.24-ht-wifi-network-optimized', 'build/examples/wireless/ns3.24-vht-wifi-network-optimized', 'build/examples/wireless/ns3.24-wifi-timing-attributes-optimized', 'build/examples/wireless/ns3.24-wifi-sleep-optimized', 'build/examples/wireless/ns3.24-power-adaptation-distance-optimized', 'build/examples/wireless/ns3.24-power-adaptation-interference-optimized', 'build/examples/wireless/ns3.24-rate-adaptation-distance-optimized', 'build/examples/wireless/ns3.24-simple-mpdu-aggregation-optimized', 'build/examples/wireless/ns3.24-simple-two-level-aggregation-optimized', 'build/examples/wireless/ns3.24-simple-ht-hidden-stations-optimized', 'build/examples/tutorial/ns3.24-hello-simulator-optimized', 'build/examples/tutorial/ns3.24-first-optimized', 'build/examples/tutorial/ns3.24-second-optimized', 'build/examples/tutorial/ns3.24-third-optimized', 'build/examples/tutorial/ns3.24-fourth-optimized', 'build/examples/tutorial/ns3.24-fifth-optimized', 'build/examples/tutorial/ns3.24-sixth-optimized', 'build/examples/tutorial/ns3.24-seventh-optimized', 'build/examples/udp-client-server/ns3.24-udp-client-server-optimized', 'build/examples/udp-client-server/ns3.24-udp-trace-client-server-optimized', 'build/examples/energy/ns3.24-energy-model-example-optimized', 'build/examples/energy/ns3.24-energy-model-with-harvesting-example-optimized', 'build/examples/ipv6/ns3.24-icmpv6-redirect-optimized', 'build/examples/ipv6/ns3.24-ping6-optimized', 'build/examples/ipv6/ns3.24-radvd-optimized', 'build/examples/ipv6/ns3.24-radvd-two-prefix-optimized', 'build/examples/ipv6/ns3.24-test-ipv6-optimized', 'build/examples/ipv6/ns3.24-fragmentation-ipv6-optimized', 'build/examples/ipv6/ns3.24-fragmentation-ipv6-two-MTU-optimized', 'build/examples/ipv6/ns3.24-loose-routing-ipv6-optimized', 'build/examples/ipv6/ns3.24-wsn-ping6-optimized', 'build/examples/stats/ns3.24-wifi-example-sim-optimized', 'build/examples/udp/ns3.24-udp-echo-optimized', 'build/examples/error-model/ns3.24-simple-error-model-optimized', 'build/scratch/ns3.24-scratch-simulator-optimized', 'build/scratch/subdir/ns3.24-subdir-optimized']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'simple-routing-ping6.py', 'realtime-udp-echo.py', 'mixed-wireless.py', 'wifi-ap.py', 'first.py', 'second.py', 'third.py']

