from ubuntu:18.04
run echo "travis_fold:start:Dapt\033[33;1mservice Dockerfile apt\033[0m" &&     apt-get -qq update && apt-get install -qq xinetd &&     echo "\ntravis_fold:end:Dapt\r"


copy speedrun-004 /
run chmod 755 /speedrun-004

run touch /flag && chmod 644 /flag && echo "OOO{Maybe ur lying to yourself. Maybe ur NoT the white hat pretending 2 be a black hat. Maybe you're the black hat pretending 2 be the white hat.}" > /flag
copy service.conf /service.conf
copy wrapper /wrapper
copy banner_fail /

expose 31337

cmd ["/usr/sbin/xinetd", "-filelog", "-", "-dontfork", "-f", "/service.conf"]

